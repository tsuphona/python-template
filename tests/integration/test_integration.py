import pytest

from core_module.sub_module1 import CoreClass1


@pytest.mark.integration
def test_add_subtract():
    a: int = 7
    b: int = 36
    c: int = 17

    sum: int = CoreClass1.add(a, b)
    actual_result: int = CoreClass1.subtract(sum, c)

    expected_result: int = 26

    assert actual_result == expected_result
