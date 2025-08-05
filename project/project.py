import json
import sys
import datetime
import os
import tabulate


FILENAME = "data/habits.json"
TODAY = datetime.date.today().strftime("%d/%m/%Y")

class Habit:
    def __init__(self, name, created=None, completed=None):
        self.name = name
        self.created = created if created else TODAY
        self.completed = completed if completed else []

    def __str__(self):
        return f"Habit {self.name} was created on {self.created}."
    
    def check(self):
        if TODAY not in self.completed:
            self.completed.append(TODAY)
    
    def uncheck(self):
        if TODAY in self.completed:
            self.completed.remove(TODAY)

    def format_json(self):
        return {
            "name": self.name,
            "created": self.created,
            "completed": self.completed
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
                
                while True:
                    
                    habits = list_all_habits()
                    table = [[i + 1, habit.name, "✅" if TODAY in habit.completed else "❌"] for i, habit in enumerate(habits)]
                    headers = ["#", "Habit", "Done Today"]
                    
                    clear_terminal()
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
                    with open(FILENAME, 'w') as file:
                        json.dump(updated, file, indent=4)
                    
            elif action == "4":
                data = list_all_habits()
                table = [[i + 1, habit["name"], habit["created"]] for i, habit in enumerate(data)]
                headers = ["#", "Habit", "Created"]
                clear_terminal()
                print("Your habits:\n")
                print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid"))
                input("Press Enter to return to menu...")

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
    
    habits = [Habit(habit["name"], habit["created"], habit["completed"]) for habit in data]
    return habits


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # windows x linux


if __name__ == "__main__":
    main()