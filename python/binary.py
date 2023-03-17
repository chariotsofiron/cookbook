def to_bin(value: int, n_bits: int = 8) -> str:
    """Convert a signed decimal value to 2s complement binary.

    :param value: The signed decimal value to convert
    :param n_bits: The number of bits to represent the result
    :return: The binary value

    Examples:
        to_bin(5, 4) -> '0101'
        to_bin(-2, 4) -> '1110'
    """
    assert -(2 ** (n_bits - 1)) <= value <= 2 ** (n_bits - 1) - 1
    return "{:0>{}b}".format(value & 2**n_bits - 1, n_bits)
