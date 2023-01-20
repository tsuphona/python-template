# -*- coding: utf-8 -*-
from . import helpers


def get_hmm() -> str:
    """Get a thought."""
    return "hmmm..."


def hmm() -> None:
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())


def add(num1: int, num2: int) -> int:
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num2 + num2


def subtract(a: int, b: int) -> int:
    """Subtract two integers"""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two floats"""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide two floats"""
    return a / b
