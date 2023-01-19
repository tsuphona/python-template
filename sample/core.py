# -*- coding: utf-8 -*-
from . import helpers


def get_hmm() -> str:
    """Get a thought."""
    return "hmmm..."


def hmm() -> None:
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())


def add(a: int, b: int) -> int:
    """Add two integers"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract two integers"""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two floats"""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide two floats"""
    return a / b
