import pytest
import sys
import json
import datetime
from .project import add_habit, remove_habit, get_habits, Habit

# pytest -s test_project.py

FILENAME = "data/pytest.json"

def main():
    test_add_habit_valid()
    test_add_habit_duplicate()
    test_add_habit_no_name()

    test_remove_habit_valid()
    test_add_habit_no_name()
    


def test_add_habit_valid():
    habit = add_habit(FILENAME, "Read")
    assert habit.name == "Read"
    assert habit.created == datetime.date.today().strftime("%d/%m/%Y")
    assert str(habit) == f"Habit {habit.name} was created on {habit.created}."


def test_add_habit_duplicate():
    with pytest.raises(ValueError, match=f"Habit 'Read' already exists."):
        habit = add_habit(FILENAME, "Read")


def test_add_habit_no_name():
    with pytest.raises(ValueError, match="Habit name cannot be empty."):
        add_habit(FILENAME, "")

"""
FileNotFoundError
json.JSONDecodeError
"""

def test_remove_habit_valid():
    habit = remove_habit(FILENAME, "Read")


def test_remove_habit_no_name():
    with pytest.raises(ValueError, match="Habit name cannot be empty."):
        remove_habit(FILENAME, "")


if __name__ == "__main__":
    main()