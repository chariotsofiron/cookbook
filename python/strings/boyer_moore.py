"""Boyer Moore algorithm.

Given a pattern, and an input string, give all the indices after which
the pattern can be found.

Example:
-------
    Given input_string = "ABBCDDBCE", pattern = "BC",
    Because input_string[2:4] == input_string[6,8] == "BC"
    return 2, 6

"""

from collections.abc import Iterator


def _preprocess(pattern: str) -> dict[str, int]:
    """Preprocess the pattern.

    Note the last occurence index of each character in the pattern.
    time: O(m)
    space: O(m)
    where m is the size of the pattern.
    """
    return {element: i for i, element in enumerate(pattern)}


def boyer_moore(input_string: str, pattern: str) -> Iterator[int]:
    """Boyer Moore algorithm.

    time: O(mn)
    space: O(m)
    note although the upperbound is the same as the brute force solution,
    it performs better for almost all inputs.
    """
    last_occurence = _preprocess(pattern)
    i = j = len(pattern) - 1
    while i <= len(input_string) - 1:
        # Match as many chars as possible from the end of the pattern
        if input_string[i] == pattern[j]:
            if j == 0:
                # All characters match!
                yield i
                # Restart algorithm starting right after the matched string.
                i = i + len(pattern)
                j = len(pattern) - 1
            else:
                i -= 1
                j -= 1
        else:
            # If the mismatched character appears in the pattern, then we
            # allign the last occurence of the character in the pattern with
            # the mismatched location. Else, we start over, the index after
            # the mismatched character.
            i += len(pattern) - min(
                j, 1 + last_occurence.get(input_string[i], -1)
            )
            j = len(pattern) - 1
            # Note: a minumum of j guarrantees we do not move so far back that
            # we start matching again from a section we've already eliminated.
