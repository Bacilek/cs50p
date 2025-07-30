import pytest
from jar import Jar


def main():
    test_init()
    test_capacity()
    test_withdraw()
    test_deposit()
    test_str()


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12


def test_capacity():
    assert Jar(0)
    assert Jar(10)
    assert Jar(100)
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar("cat")


# just deposit error, rest is in test_str()
def test_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)


# just withdraw error, rest is in test_str()
def test_withdraw():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(5) == "🍪🍪🍪🍪🍪"


if __name__ == "__main__":
    main()
