from hello import hello

def test_default():
    assert hello() == "hello, world"


def test_name():
    assert hello("Mark") == "hello, Mark"