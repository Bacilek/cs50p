import json
import sys
import datetime
import os
import tabulate


FILENAME = "data/habits.json"

class Habit:
    def __init__(self, name):
        self.name = name
        self.name = name
        self.created = datetime.date.today().strftime("%d/%m/%Y")

    def __str__(self):
        return f"Habit {self.name} was created on {self.created}."
    
    def mark_done(self):
        pass
    
    def unmark_done(self):
        pass

    def format_json(self):
        return {
            "name": self.name,
            "created": self.created,
            "completed": []
        }


def main():
    if len(sys.argv) != 1:
        sys.exit("Usage: python project.py")
    
    while True:
        clear_terminal()
        username = input("Enter your username: ")
        if username.strip():
            break
    
    
    while True:
        clear_terminal()
        print(f"Welcome back, {username}!")
        print("1. Add a habit")
        print("2. Remove a habit")
        print("3. List today's habits")
        print("4. List all habits")
        print("5. Exit")
        
        action = input("> ")
        
        try:
            if action == "1":
                habit = add_habit() # TODO returns
            elif action == "2":
                habit = remove_habit() # TODO returns
            elif action == "3":
                habit = remove_habit() # TODO
            elif action == "4":
                list_all_habits()
            elif action == "5":
                clear_terminal()
                print(f"Goodbye, {username}")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            clear_terminal()
            print(f"Error: {e}")
            input("Press Enter to continue...")


def add_habit(name=None):
    clear_terminal()
    print("Add a habit")
    
    if name is None:
        name = input("Habit name: ")

    if name.strip() == "":
        raise ValueError("Habit name cannot be empty.")

    os.makedirs("data", exist_ok=True)
    
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else: 
        data = []

    if any(habit["name"].lower() == name.lower() for habit in data):
        raise ValueError(f"Habit '{name}' already exists.")
    
    habit = Habit(name)
    data.append(habit.format_json())

    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Habit '{habit.name}' added successfully.")

    return habit


def remove_habit(name=None):
    clear_terminal()
    print("Remove a habit")
    
    if not os.path.exists(FILENAME):
        raise FileNotFoundError("/data/habits.json does not exist.")

    with open(FILENAME, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Habits data is corrupted.")
    
    if not data:
        print("You don't have any habits yet, first add one!")
        input("Press Enter to return to menu...")
        return ValueError("No habits to remove.")
    
    if name is None:
        name = input("Habit name: ")

    if name.strip() == "":
        raise ValueError("Habit name cannot be empty.")

    # Find habit by name
    for i, habit in enumerate(data):
        if habit["name"].lower() == name.lower():
            del data[i]
            with open(FILENAME, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Habit '{name}' removed successfully.")
            input("Press Enter to return to menu...")
            return habit

    raise LookupError(f"Habit '{name}' not found.")


def list_all_habits():
    clear_terminal()
    print("Your habits:\n")

    if not os.path.exists(FILENAME):
        print("/data/habits.json file containing habits does not exist.")
        input("Press Enter to return to menu...")
        return

    with open(FILENAME, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("Habits data is corrupted.")
            input("Press Enter to return to menu...")
            return

    if not data:
        print("You don't have any habits yet, first add one!")
        input("Press Enter to return to menu...")
        return

    # Format table
    table = [[i + 1, habit["name"], habit["created"]] for i, habit in enumerate(data)]
    headers = ["#", "Habit", "Created"]

    print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid"))
    print()
    input("Press Enter to return to menu...")


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # windows x linux


if __name__ == "__main__":
    main()