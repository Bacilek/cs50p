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
    if len(sys.argv) != 1:
        sys.exit("Usage: python project.py")
    
    username, filename = login()
    
    while True:
        option = display_options(username)
        
        try:
            if option == "1":
                habit = add_habit(filename)

            elif option == "2":
                habit = remove_habit(filename)

            elif option == "3":
                while True:
                    habits = get_habits(filename)
                    table = [
                        [i + 1, habit.name, "✅" if TODAY in habit.completed else "❌"]
                        for i, habit in enumerate(habits)
                        ]
                    headers = ["#", "Name", "Today's status"]
                    
                    clear_terminal()
                    if habits == []:
                        break
                    print("Today's habits:")                    
                    print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid"))

                    try:
                        id = int(input("Select habit # to toggle (0 to exit): "))
                        if id == 0:
                            break
                        habit = habits[id - 1]
                        if TODAY in habit.completed:
                            habit.uncheck()
                        else:
                            habit.check()
                    except (ValueError, IndexError):
                        clear_terminal()
                        print("Invalid Selection.")
                        input("Press Enter to continue...")
                    
                    updated = [habit.format_json() for habit in habits]
                    with open(filename, 'w') as file:
                        json.dump(updated, file, indent=4)
                    
            elif option == "4":
                habits = get_habits(filename)
                
                table = [
                    [habit.name, habit.description, habit.existence, f"{habit.consistency:.0%}"]
                    for habit in habits
                    ]
                headers = ["Name", "Description", "Existence (days)", "Consistency"]
                clear_terminal()
                if habits == []:
                    continue
                print("Your habits:")
                print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid"))
                input("Press Enter to return to menu...")

            elif option == "5":
                clear_terminal()
                print(f"Goodbye, {username}")
                break

            else:
                print("Invalid choice.")
        except Exception as e:
            clear_terminal()
            print(f"Error: {e}")
            input("Press Enter to continue...")


def login():
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


def display_options(username):
    clear_terminal()
    print(f"Welcome back, {username}!")
    print("1. Add a habit")
    print("2. Remove a habit")
    print("3. List today's habits")
    print("4. List all habits")
    print("5. Exit")
    
    return input("> ")


def add_habit(filename, name=None):
    
    clear_terminal()
    print("Add a habit")
    
    name = input("Habit name: ").strip()
    description = input("Habit description: ")

    # Non-empty habit name
    if name == "":
        raise ValueError("Habit name cannot be empty.")
    
    # 1+ letter in habit name
    pattern = r"(?=.*[A-Za-z]).*"
    if not re.fullmatch(pattern, name):
        raise ValueError("Habit name must contain at least one letter.")

    os.makedirs("data", exist_ok=True)  # create data directory if it doesn't exist
    
    # Check if file exists, if not create it
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    # Check for duplicates
    if any(habit["name"].lower() == name.lower() for habit in data):
        raise ValueError(f"Habit '{name}' already exists.")
    
    # Create new habit
    habit = Habit(name, description)
    data.append(habit.format_json())
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Habit '{habit.name}' with description '{habit.description}' added successfully.")
    input("Press Enter to return to menu...")

    return habit


def remove_habit(filename, name=None):
    clear_terminal()

    # File exists
    if not os.path.exists(filename):
        raise FileNotFoundError("/data/habits.json does not exist.")

    # Load file
    with open(filename, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Habits data is corrupted.")
    
    # No habits
    if not data:
        print("You don't have any habits yet, first add one!")
        input("Press Enter to return to menu...")
        return ValueError("No habits to remove.")
    
    # Display habits
    habits = get_habits(filename)
    table = [
        [i + 1, habit.name]
        for i, habit in enumerate(habits)
        ]
    headers = ["#", "Name"]
    print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid"))
    
    # Manual
    if name is None:
        name = input("Select habit # or name to remove (0 to exit): ")

    # No name provided
    if name.strip() == "":
        raise ValueError("Invalid habit name.")

    # Find Habit
    pattern = r"(?=.*[A-Za-z]).*"
    # By name
    if re.fullmatch(pattern, name):
        for i, habit in enumerate(data):
            if habit["name"].lower() == name.lower():
                del data[i]
                with open(filename, 'w') as file:
                    json.dump(data, file, indent=4)
                print(f"Habit '{name}' removed successfully.")
                input("Press Enter to return to menu...")
                return habit
    # By index
    else:
        try:
            index = int(name) - 1
            if 0 <= index < len(data):
                removed_habit = data.pop(index)
                with open(filename, 'w') as file:
                    json.dump(data, file, indent=4)
                print(f"Habit '{removed_habit['name']}' removed successfully.")
                input("Press Enter to return to menu...")
                return Habit(**removed_habit)
        except (ValueError, IndexError):
            pass
    
    raise LookupError(f"Habit '{name}' not found.")


def get_habits(filename):

    # File exists
    if not os.path.exists(filename):
        clear_terminal()
        print("/data/habits.json file containing habits does not exist.")
        input("Press Enter to return to menu...")
        return []
    
    # Load file
    with open(filename, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            clear_terminal()
            print("Habits data is corrupted.")
            input("Press Enter to return to menu...")
            return []  # None? | ""?

    # No habits
    if not data:
        clear_terminal()
        print("You don't have any habits yet, first add one!")
        input("Press Enter to return to menu...")
        return []
    
    # json to list of Habit objects
    habits = [
        Habit(
            habit["name"], 
            habit.get("description", ""), 
            habit["created"], 
            habit["completed"]
    ) for habit in data]

    return habits


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
    os.system('cls' if os.name == 'nt' else 'clear')  # windows x linux


if __name__ == "__main__":
    main()