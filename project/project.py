# --------------------- Imports ---------------------

import json
import sys
import datetime
import os
import tabulate
import csv
import re
from pwinput import pwinput  # type: ignore
from habit import Habit


# --------------------- Constants ---------------------

TODAY = datetime.date.today().strftime("%d/%m/%Y")
USERS_FILE = "data/users.csv"

# --------------------- Main Loop ---------------------

def main():
    """Main function to run the Habit Tracker application."""
    
    # Check command line arguments
    if len(sys.argv) != 1:
        sys.exit("Usage: python project.py")

    username, filename = login()

    while True:
        option = display_options(username)

        if option == "1":
            add_habit_ui(filename)
        elif option == "2":
            remove_habit_ui(filename)
        elif option == "3":
            list_today_ui(filename)
        elif option == "4":
            list_all_ui(filename)
        elif option == "5":
            clear_terminal()
            print(f"Goodbye, {username}")
            break
        else:
            input("Invalid choice. Press Enter to continue...")

# --------------------- File Utilities ---------------------

def load_json(path, default=None):
    """Load JSON data from a file."""

    # user data file exists
    if not os.path.exists(path):
        return default

    # load & return user data
    with open(path, 'r') as file:
        # user data file not corrupted
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return default


def save_json(path, data):
    """Save JSON data to a file."""
    
    os.makedirs(os.path.dirname(path), exist_ok=True)  # dir exists | create it 
    
    # save user data
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


def load_users():
    """Load users from the USERS_FILE."""
    
    # users.json eixsts | create it
    if not os.path.exists(USERS_FILE):
        os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
        
        # suers.json header
        with open(USERS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["username", "password"])
            writer.writeheader()
        return {}

    # load users
    with open(USERS_FILE, "r") as f:
        reader = csv.DictReader(f)
        return {row["username"]: row["password"] for row in reader}


def save_user(username, password):
    """Save a new user to the USERS_FILE."""
    users = load_users()
    
    # add new user into users.json
    if username not in users:
        with open(USERS_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["username", "password"])
            writer.writerow({"username": username, "password": password})


# --------------------- User Authentication ---------------------

def validate_password(password):
    """Validate: 5+ chars, 1 uppercase, 1 lowercase, 1 number, no whitespace"""
    pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)\S{5,}"
    return bool(re.fullmatch(pattern, password))


def login():
    """Handle user login or registration."""
    users = load_users()

    # 
    while True:
        clear_terminal()
        print("Welcome to Habit Tracker!")
        username = input("Username: ").strip()
        
        # invalid username
        if not username:
            input("Invalid username. Press Enter to try again...")
            continue

        password = pwinput("Password: ")

        # old user
        if username in users:
            # incorrect password
            if users[username] != password:
                input("Wrong password. Press Enter to try again...")
                continue
        # new user
        else:
            if not validate_password(password):
                input(
                    "Minimum password length is 5 characters: must include uppercase, lowercase, number and no spaces. Press Enter..."
                )
                continue
            save_user(username, password)

        # create empty user file if it doesn't exist
        user_file = f"data/{username}.json"
        if not os.path.exists(user_file):
            save_json(user_file, [])

        return username, user_file


# --------------------- Habit Data logic ---------------------

def get_habits(filename):
    """Load habits from a JSON file and return a list of Habit objects."""
    data = load_json(filename)
    return [Habit(h["name"], h.get("description", ""), h["created"], h.get("completed", [])) for h in data]


def add_habit_data(filename, name, description):
    """Add a new habit to the JSON file and return the Habit object."""
    data = load_json(filename)
    
    # check for duplicate habit
    if any(h["name"].lower() == name.lower() for h in data):
        raise ValueError(f"Habit '{name}' already exists.")

    # create new habit & save it into user data file
    habit = Habit(name, description)
    data.append(habit.format_json())
    save_json(filename, data)

    return habit


def remove_habit_data(filename, identifier):
    """Remove a habit by name or index from the JSON file."""
    
    # no habits in user data file
    data = load_json(filename)
    if not data:
        raise ValueError("No habits to remove.")

    # remove by name
    for i, h in enumerate(data):
        if h["name"].lower() == str(identifier).lower():
            removed = data.pop(i)
            save_json(filename, data)
            return Habit(**removed)  # dictionary unpacking

    # remove by #
    try:
        idx = int(identifier) - 1
        if 0 <= idx < len(data):
            removed = data.pop(idx)
            save_json(filename, data)
            return Habit(**removed)  # dictionary unpacking
    except ValueError:
        pass

    raise LookupError(f"Habit '{identifier}' not found.")


# --------------------- UI ---------------------

def display_options(username):
    """Display the main menu options and return the user's choice."""
    clear_terminal()
    print(f"Welcome back, {username}!")
    print("1. Add a habit")
    print("2. Remove a habit")
    print("3. List today's habits")
    print("4. List all habits")
    print("5. Exit")
    return input("> ").strip()


def add_habit_ui(filename):
    """UI for adding a new habit."""
    clear_terminal()
    print("Add a habit")
    
    # get habit data
    name = input("Habit name: ").strip()
    description = input("Habit description: ")

    # 1+ letter
    if not name or not re.search(r"[A-Za-z]", name):
        input("Habit name must contain at least one letter. Press Enter...")
        return

    # add habit
    try:
        habit = add_habit_data(filename, name, description)
        print(f"Habit '{habit.name}' added successfully!")
    except ValueError as e:
        print(e)
    input("Press Enter to return to menu...")


def remove_habit_ui(filename):
    """UI for removing a habit."""
    clear_terminal()
    habits = get_habits(filename)
    
    # no habits in user data file
    if not habits:
        input("No habits to remove. Press Enter...")
        return

    # display habits
    table = [[i + 1, h.name] for i, h in enumerate(habits)]
    print(tabulate.tabulate(table, headers=["#", "Name"], tablefmt="fancy_grid"))
    
    # select habit to remove
    identifier = input("Select habit # or name to remove (0 to exit): ").strip()
    if identifier == "0":
        return

    # remove habit
    try:
        removed = remove_habit_data(filename, identifier)
        print(f"Habit '{removed.name}' removed successfully!")
    except (ValueError, LookupError) as e:
        print(e)
    input("Press Enter to return to menu...")


def list_today_ui(filename):
    """UI for listing today's habits and toggling their status."""
    clear_terminal()
    
    
    while True:
        habits = get_habits(filename)
        
        if empty_user_data_file(habits):
            return
        
        # display today's habits
        table = [[i + 1, h.name, "✅" if TODAY in h.completed else "❌"] for i, h in enumerate(habits)]
        print(tabulate.tabulate(table, headers=["#", "Name", "Today's status"], tablefmt="fancy_grid"))

        # toggle habit status
        try:
            selection = int(input("Select habit # to toggle (0 to exit): "))
            if selection == 0:
                break
            habit = habits[selection - 1]
            habit.check() if TODAY not in habit.completed else habit.uncheck()
        except (ValueError, IndexError):
            print("Invalid selection.")
            input("Press Enter to continue...")

        # save updated habit statuses
        save_json(filename, [h.format_json() for h in habits])
        clear_terminal()


def list_all_ui(filename):
    """UI for listing all habits."""
    clear_terminal()
    habits = get_habits(filename)
    
    if empty_user_data_file(habits):
        return

    table = [[h.name, h.description, h.existence, f"{h.consistency:.0%}"] for h in habits]
    print(tabulate.tabulate(table, headers=["Name", "Description", "Existence (days)", "Consistency"], tablefmt="fancy_grid"))
    input("Press Enter to return to menu...")


def empty_user_data_file(habits):
    if not habits:
        input("No habits yet. Press Enter to return...")
        return True
    return False

# --------------------- Utils ---------------------

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')  # windows x linux

if __name__ == "__main__":
    main()