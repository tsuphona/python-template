# -*- coding: utf-8 -*-

from .context import sample


def test_add_multiply_divide() -> None:
    sum = sample.add(5, 1)
    factor = sample.multiply(6, 6)
    assert sample.divide(factor, sum) == 6
