import pytest

from calc import divide


@pytest.mark.slow
def test_divide():
    assert divide(6, 3) == 2
