from calc import add, scale


def test_add():
    assert add(2, 2) == 4


def test_scale():
    assert scale(3) == 6
