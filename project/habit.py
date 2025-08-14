import datetime

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

        self.consistency = float((len(self.completed) / self.existence))  # %

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
        