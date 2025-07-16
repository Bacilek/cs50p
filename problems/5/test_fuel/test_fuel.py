import pytest
from fuel import convert, gauge

def main():
    test_convert_incorrect()
    test_convert_errors()
    test_gauge_labels()


def test_convert_incorrect():
    assert convert("1/5") == 20
    assert convert("1/3") == 33


def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("-1/1")


def test_gauge_labels():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(33) == "33%"
    assert gauge(66) == "66%"
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'


if __name__ == "__main__":
    main()
