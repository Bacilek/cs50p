import json
import sys
import datetime
import os
import tabulate


class Habit:
    def __init__(self, name):
        if name == "":
            raise ValueError("Habit name cannot be empty")
        self.name = name
        self.created = datetime.date.today().strftime("%d/%m/%Y")

    def __str__(self):
        return f"Habit {self.name} was created on {self.created}."
    
    def mark_done(self):
        pass
    
    def unmark_done(self):
        pass

    def format(self):
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
        print("1. List habits")
        print("3. Exit")
        
        action = input("> ")
        if action == "1":
            add_habit()
        elif action == "2":
            list_habits()
        elif action == "3":
            print(f"Goodbye, {username}")
            break
        else:
            print("Invalid choice.")


def add_habit():
    clear_terminal()
    print("Add a new habit")
    new_name = input("New habit name: ")
    if new_name.strip() == "":
        print("Habit name cannot be empty.")
        input("Press Enter to continue...")
        return

    os.makedirs("data", exist_ok=True)
    filename = "data/habits.json"
    
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    if any(habit["name"].lower() == new_name.lower() for habit in data):
        print(f"Habit '{new_name}' already exists. Please choose a different name.")
        input("Press Enter to continue...")
        return
    
    habit = Habit(new_name)
    data.append(habit.format())

    with open("data/habits.json", 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Habit '{habit.name}' added successfully.")
    input("Press enter to continue...")


def remove_habit():
    pass


def list_habits():
    pass


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # windows x linux


if __name__ == "__main__":
    main()