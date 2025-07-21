import pytest
from working import convert

def main():
    test_valid()
    test_invalid()
    test_twelves()


def test_valid():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("10:00 AM to 12:60 PM")
    with pytest.raises(ValueError):
        convert("25:00 PM to 12:00 AM")
    with pytest.raises(ValueError):
        convert("10:00AM10:00PM")


def test_twelves():
    assert convert("12:00 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"



if __name__ == "__main__":
    main()
