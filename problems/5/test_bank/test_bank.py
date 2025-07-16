from bank import value

def main():
    test_zero()
    test_twenty()
    test_hundred()


def test_zero():
    assert value("HeLlO?") == 0
    assert value("HELLO PLEASE HELP ME IM UNDER THE WATER") == 0


def test_twenty():
    assert value("Hi") == 20
    assert value("Heya, my brother") == 20
    assert value("How ya doin'?") == 20


def test_hundred():
    assert value("Top of the morning to ya") == 100
    assert value("Insert hello") == 100
    assert value("soooo, hi? I guess") == 100


if __name__ == "__main__":
    main()
