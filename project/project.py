import json
import sys
import datetime
import os
import tabulate

TODAY = datetime.date.today().strftime("%d/%m/%Y")

class Habit:
    def __init__(self, name, description=None, created=None, completed=None):
        self.name = name
        self.description = description if description else ""
        self.created = created if created else TODAY
        self.completed = completed if completed else []
        
        today = datetime.date.today()
        created_date = datetime.datetime.strptime(self.created, "%d/%m/%Y").date()
        self.existence = (today - created_date).days + 1  # habit existence [days]

        self.consistency = float((len(self.completed) / self.existence))  # percentual consistency

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
            "description": self.description,
            "created": self.created,
            "completed": self.completed
        }
        

def main():
    if len(sys.argv) != 1:
        sys.exit("Usage: python project.py")
    
    while True:
        clear_terminal()
        print("Welcome to Habit Tracker!")
        
        global username
        username = input("Enter your username: ").strip()
        
        if username:
            filename = f"data/{username}.json"
            os.makedirs("data", exist_ok=True)
            
            if not os.path.exists(filename):
                with open(filename, 'w') as file:
                    json.dump([], file, indent=4)
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
                habit = add_habit(filename)

            elif action == "2":
                habit = remove_habit(filename)

            elif action == "3":
                while True:
                    habits = list_all_habits(filename)
                    table = [
                        [i + 1, habit.name, "✅" if TODAY in habit.completed else "❌"]
                        for i, habit in enumerate(habits)
                        ]
                    headers = ["#", "Habit", "Today's status"]
                    
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
                    with open(filename, 'w') as file:
                        json.dump(updated, file, indent=4)
                    
            elif action == "4":
                habits = list_all_habits(filename)
                table = [
                    [habit.name, habit.description, habit.existence, f"{habit.consistency:.0%}"]
                    for habit in habits
                    ]
                headers = ["Habit", "Description", "Existence (days)", "Consistency"]
                clear_terminal()
                print("Your habits:")
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


def add_habit(filename, name=None):
    
    clear_terminal()
    print("Add a habit")
    
    name = input("Habit name: ")
    description = input("Habit description: ")

    if name.strip() == "":
        raise ValueError("Habit name cannot be empty.")

    os.makedirs("data", exist_ok=True)  # create data directory if it doesn't exist
    
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

    if any(habit["name"].lower() == name.lower() for habit in data):
        raise ValueError(f"Habit '{name}' already exists.")
    
    habit = Habit(name, description)
    data.append(habit.format_json())

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Habit '{habit.name}' with description '{habit.description}' added successfully.")

    return habit


def remove_habit(filename, name=None):
    clear_terminal()
    print("Remove a habit")
    
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
    
    if name is None:
        name = input("Habit name: ")

    if name.strip() == "":
        raise ValueError("Habit name cannot be empty.")

    # Find habit by name
    for i, habit in enumerate(data):
        if habit["name"].lower() == name.lower():
            del data[i]
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Habit '{name}' removed successfully.")
            input("Press Enter to return to menu...")
            return habit

    raise LookupError(f"Habit '{name}' not found.")


def list_all_habits(filename):
    if not os.path.exists(filename):
        print("/data/habits.json file containing habits does not exist.")
        input("Press Enter to return to menu...")
        return

    with open(filename, 'r') as file:
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
    
    habits = [Habit(
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