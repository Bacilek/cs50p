from twttr import shorten

def main():
    test_empty()
    test_same()
    test_change()
    test_uppercase()
    test_sentence()


def test_empty():
    assert shorten("") == ""


def test_same():
    assert shorten("twttr") == "twttr"


def test_change():
    assert shorten("twitter") == "twttr"
    assert shorten("mara") == "mr"


def test_uppercase():
    assert shorten("MARA") == "MR"


def test_sentence():
    assert shorten("Lorem ipsum.") == "Lrm psm."


def test_numbers():
    assert shorten("123456789") == "123456789"


if __name__ == "__main__":
    main()
