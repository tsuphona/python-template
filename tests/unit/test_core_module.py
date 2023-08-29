import pytest

from core_module.sub_module1 import CoreClass1
from core_module.sub_module2 import CoreClass2


@pytest.mark.unit
def test_add():
    a: int = 2
    b: int = 3
    actual_sum: int = CoreClass1.add(a, b)

    expected_sum: int = 5

    assert actual_sum == expected_sum


@pytest.mark.unit
def test_subtract():
    a: int = 10
    b: int = 7
    actual_difference: int = CoreClass1.subtract(a, b)

    expected_difference: int = 3

    assert actual_difference == expected_difference


@pytest.mark.unit
def test_multiply():
    a: float = 1.5
    b: float = 2.0
    actual_product: float = CoreClass2.multiply(a, b)

    expected_product: int = 3.0

    assert actual_product == expected_product


@pytest.mark.unit
def test_divide():
    a: float = 10.0
    b: float = 2.0
    actual_quotient: float = CoreClass2.divide(a, b)

    expected_quotient: int = 5.0

    assert actual_quotient == expected_quotient
