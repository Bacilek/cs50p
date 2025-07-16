from plates import is_valid

def main():
    test_length()
    test_start()
    test_first_number_zero()
    test_number_in_middle()
    test_punctuation()


def test_length():
    assert not is_valid("a")
    assert is_valid("aaaa")
    assert not is_valid("aaaaaaa")


def test_start():
    assert not is_valid("50CS")
    assert not is_valid("5CS0")
    assert not is_valid("C50S")
    assert is_valid("CS50")
    assert not is_valid("5")
    assert not is_valid("A")
    assert is_valid ("cs")
    assert not is_valid("c123")


def test_first_number_zero():
    assert not is_valid("CS05")


def test_number_in_middle():
    assert not is_valid("CS50CS")


def test_punctuation():
    assert not is_valid("cs:50")
    assert not is_valid("cs50!")


if __name__ == "__main__":
    main()
