import pytest
from um import count

def main():
    test_count()
    test_case()
    test_inside_word()
    test_whitespace()
    test_punctuation()


def test_count():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("um um um") == 3
    assert count("um um um um") == 4
    assert count("um um um um um") == 5


def test_case():
    assert count("UM um Um uM") == 4


def test_inside_word():
    assert count("yummy") == 0
    assert count("name's Umma") == 0


def test_whitespace():
    assert count(" um") == 1
    assert count("um  ") == 1
    assert count("  um ") == 1


def test_punctuation():
    assert count("Um, thanks, um...for the album") == 2
    assert count("!um?") == 1


if __name__ == "__main__":
    main()
