"""Fizzbuzz."""


def fizzbuzz(n: int) -> str:
    """Fizzbuzz."""
    output = ""
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            output += "FizzBuzz\n"
        elif i % 3 == 0:
            output += "Fizz\n"
        elif i % 5 == 0:
            output += "Buzz\n"
        else:
            output += str(i) + "\n"
    return output


def fizzbuzz_no_modulo(n: int) -> str:
    """No modulo."""
    a = 3
    b = 5

    output = ""
    for i in range(1, n):
        line = ""
        if i == a:
            line += "Fizz"
            a += 3
        if i == b:
            line += "Buzz"
            b += 5
        if line == "":
            line = str(i)
        output += line + "\n"
    return output


def test() -> None:
    """Runs the tests."""
    expected = (
        "1\n"
        "2\n"
        "Fizz\n"
        "4\n"
        "Buzz\n"
        "Fizz\n"
        "7\n"
        "8\n"
        "Fizz\n"
        "Buzz\n"
        "11\n"
        "Fizz\n"
        "13\n"
        "14\n"
        "FizzBuzz\n"
    )
    assert fizzbuzz(16) == expected
    assert fizzbuzz_no_modulo(16) == expected
