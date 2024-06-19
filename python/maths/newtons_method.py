"""Newton's method."""

from typing import Callable


def newtons(
    func: Callable,
    f_prime: Callable,
    guess: float,
    *,
    n_steps: int = 20,
    epsilon: float = 0.0001,
) -> float:
    """Returns the zero of the function func using Newton's method.

    Args:
    ----
    func: the function to find roots for
    f_prime: the derivative of func
    guess: the initial guess
    n_steps: the number of iterations
    epsilon: the tolerance

    """
    for _ in range(n_steps):
        guess -= func(guess) / f_prime(guess)
        if abs(func(guess)) < epsilon:
            break

    return guess


def test() -> None:
    """Tests newtons method."""
    func = lambda x: x**2 - 612  # noqa: E731
    f_prime = lambda x: 2 * x  # noqa: E731
    root = 24.7386
    assert round(newtons(func, f_prime, 10), 4) == root
    assert round(newtons(func, f_prime, -10), 4) == -root
