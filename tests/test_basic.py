# -*- coding: utf-8 -*-

from .context import sample


def test_add_small_integers() -> None:
    assert sample.add(2, 3) == 5


def test_add_large_integers() -> None:
    assert sample.add(12345, 5432) == 17777


def test_multiply() -> None:
    assert sample.multiply(7, 9) == 63


def test_divide() -> None:
    assert sample.divide(25, 5) == 5
