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
USERS = "data/users.csv"

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
    while True:
        clear_terminal()
        print("Welcome to Habit Tracker!")
        print("Please login to continue.")

        username = input("Username: ")
        if not username.strip():
            clear_terminal()
            input("Invalid username, please try again")
            continue
        
        password = pwinput("Password: ")
    
        if len(password) < 5:
            clear_terminal()
            input("Password must have length of at least 5, please try again")
            continue
        
        # lowercase, uppercase, and number in 5+ non-whitespace characters
        pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)\S{5,}"
        if not re.fullmatch(pattern, password):
            clear_terminal()
            input("Password must include at least one uppercase letter, one lowercase letter and a number, please try again.")
            continue
        
        file_exists = os.path.exists(USERS)
        
        if not file_exists:
            with open(USERS, 'w') as file:
                writer = csv.DictWriter(file, fieldnames=["username", "password"])
                writer.writeheader()

        with open(USERS, 'r') as file:
            reader = csv.DictReader(file)
            users = {row["username"]: row["password"] for row in reader}
            
        if username in users.keys():
            if users.get(username) != password:
                clear_terminal()
                input("Wrong password, please try again...")
                continue
        else:
            with open(USERS, 'a') as file:
                writer = csv.DictWriter(file, fieldnames=["username", "password"])
                writer.writerow({"username": username, "password": password})
        
        if username:
            filename = f"data/{username}.json"
            os.makedirs("data", exist_ok=True)
            
            if not os.path.exists(filename):
                with open(filename, 'w') as file:
                    json.dump([], file, indent=4)
            break

    return username, filename


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

    if not os.path.exists(filename):
        raise FileNotFoundError("/data/habits.json does not exist.")

    with open(filename, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Habits data is corrupted.")
    
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

    pattern = r"(?=.*[A-Za-z]).*"
    if re.fullmatch(pattern, name):
        # Find habit by name
        for i, habit in enumerate(data):
            if habit["name"].lower() == name.lower():
                del data[i]
                with open(filename, 'w') as file:
                    json.dump(data, file, indent=4)
                print(f"Habit '{name}' removed successfully.")
                input("Press Enter to return to menu...")
                return habit
    else:
        # Find habit by index
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


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # windows x linux


if __name__ == "__main__":
    main()