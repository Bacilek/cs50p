import json
import sys
import datetime
import os
import tabulate
import csv
import re
from pwinput import pwinput  # type: ignore
from habit import Habit

TODAY = datetime.date.today().strftime("%d/%m/%Y")
USERS_FILE = "data/users.csv"


def main():
    """Main function to run the Habit Tracker application."""
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


def login():
    """Handle user login or registration."""
    users = load_users()

    while True:
        clear_terminal()
        print("Welcome to Habit Tracker!")
        username = input("Username: ").strip()
        if not username:
            input("Invalid username. Press Enter to try again...")
            continue

        password = pwinput("Password: ")

        if username in users:
            if users[username] != password:
                input("Wrong password. Press Enter to try again...")
                continue
        else:
            if not validate_password(password):
                input(
                    "Password must be 5+ chars, include uppercase, lowercase, number, no spaces. Press Enter..."
                )
                continue
            save_user(username, password)

        # Ensure user JSON exists
        user_file = f"data/{username}.json"
        if not os.path.exists(user_file):
            save_json(user_file, [])

        return username, user_file

def load_json(path, default=None):
    """Load JSON data from a file."""
    if not os.path.exists(path):
        return default
    with open(path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return default


def save_json(path, data):
    """Save JSON data to a file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


def load_users():
    """Load users from the USERS_FILE."""
    if not os.path.exists(USERS_FILE):
        os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
        with open(USERS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["username", "password"])
            writer.writeheader()
        return {}
    with open(USERS_FILE, "r") as f:
        reader = csv.DictReader(f)
        return {row["username"]: row["password"] for row in reader}



def save_user(username, password):
    """Save a new user to the USERS_FILE."""
    users = load_users()
    if username not in users:
        with open(USERS_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["username", "password"])
            writer.writerow({"username": username, "password": password})


def validate_password(password):
    """Validate: 5+ chars, 1 uppercase, 1 lowercase, 1 number, no whitespace"""
    pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)\S{5,}"
    return bool(re.fullmatch(pattern, password))



def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')  # windows x linux



def get_habits(filename):
    """Load habits from a JSON file and return a list of Habit objects."""
    data = load_json(filename)
    return [Habit(h["name"], h.get("description", ""), h["created"], h.get("completed", [])) for h in data]

def add_habit_data(filename, name, description) -> Habit:
    data = load_json(filename)
    if any(h["name"].lower() == name.lower() for h in data):
        raise ValueError(f"Habit '{name}' already exists.")
    habit = Habit(name, description)
    data.append(habit.format_json())
    save_json(filename, data)
    return habit


def remove_habit_data(filename, identifier):
    """Remove a habit by name or index from the JSON file."""
    data = load_json(filename)
    if not data:
        raise ValueError("No habits to remove.")

    # by name
    for i, h in enumerate(data):
        if h["name"].lower() == str(identifier).lower():
            removed = data.pop(i)
            save_json(filename, data)
            return Habit(**removed)

    # by index
    try:
        idx = int(identifier) - 1
        if 0 <= idx < len(data):
            removed = data.pop(idx)
            save_json(filename, data)
            return Habit(**removed)
    except ValueError:
        pass

    raise LookupError(f"Habit '{identifier}' not found.")

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
    name = input("Habit name: ").strip()
    description = input("Habit description: ")

    if not name or not re.search(r"[A-Za-z]", name):
        input("Habit name must contain at least one letter. Press Enter...")
        return

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
    if not habits:
        input("No habits to remove. Press Enter...")
        return

    table = [[i + 1, h.name] for i, h in enumerate(habits)]
    print(tabulate.tabulate(table, headers=["#", "Name"], tablefmt="fancy_grid"))
    identifier = input("Select habit # or name to remove (0 to exit): ").strip()
    if identifier == "0":
        return

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
        if not habits:
            break

        table = [[i + 1, h.name, "✅" if TODAY in h.completed else "❌"] for i, h in enumerate(habits)]
        print(tabulate.tabulate(table, headers=["#", "Name", "Today's status"], tablefmt="fancy_grid"))

        try:
            selection = int(input("Select habit # to toggle (0 to exit): "))
            if selection == 0:
                break
            habit = habits[selection - 1]
            habit.check() if TODAY not in habit.completed else habit.uncheck()
        except (ValueError, IndexError):
            print("Invalid selection.")
            input("Press Enter to continue...")

        save_json(filename, [h.format_json() for h in habits])
        clear_terminal()



def list_all_ui(filename):
    """UI for listing all habits."""
    clear_terminal()
    habits = get_habits(filename)
    if not habits:
        input("No habits yet. Press Enter to return...")
        return
    table = [[h.name, h.description, h.existence, f"{h.consistency:.0%}"] for h in habits]
    print(tabulate.tabulate(table, headers=["Name", "Description", "Existence (days)", "Consistency"], tablefmt="fancy_grid"))
    input("Press Enter to return to menu...")



if __name__ == "__main__":
    main()