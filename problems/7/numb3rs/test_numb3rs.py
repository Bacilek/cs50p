from numb3rs import validate

def main():
    test_ranges()
    test_number_of_octets()
    test_data_types()


def test_number_of_octets():
    assert not validate("1.1.1")
    assert validate("1.1.1.1")
    assert not validate("1.1.1.1.1")


def test_ranges():
    assert not validate("-1.1.1.1")
    assert not validate("1.256.1.1")
    assert not validate("1.1.512.1")
    assert not validate("1.1.1.1024")


def test_data_types():
    assert not validate("cat.dog.rabbit.turtle")


if __name__ == "__main__":
    main()
