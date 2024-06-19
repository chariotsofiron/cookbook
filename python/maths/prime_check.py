"""Prime checking."""


def prime_check(n: int) -> bool:
    """Returns True if n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:  # noqa: PLR2004
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    j = 5
    while j * j <= n:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    return True
