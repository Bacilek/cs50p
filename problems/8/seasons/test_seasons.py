import pytest
from seasons import date_to_text
from datetime import date

def main():
    test_calculate()


def test_calculate():
    assert date_to_text(date(2025, 7, 30), date(2024, 7, 30)) == "five hundred twenty-five thousand, six hundred"
    assert date_to_text(date(2025, 7, 30), date(2023, 7, 30)) == "one million, fifty-two thousand, six hundred forty"
    assert date_to_text(date(2025, 7, 30), date(2000, 12, 31)) == "twelve million, nine hundred twenty-six thousand, eight hundred eighty"


if __name__ == "__main__":
    main()
