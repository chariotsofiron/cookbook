"""Index of permutation.

let K be number of unique elements in the sequence
let N[K] be count of each unique element in the sequence
    e.g. AAABBC => N[K] = [3, 2, 1]
let N be sum of N[K]

every legal permutation of the sequence corresponds to a path
in a M-ary tree.

permutation index corresponds to the index of the tree in
a post-order traversal of the m-ary tree.

number of terminal nodes lexicographically less than the current node
is number of permutations using the unused elements in the sequence

e.g. permutation of BAABCA

- less than B => 5!/2!2!1! = 30
- less than A => 0
- less than A => 0
- less than B => 2!/1!1! = 2
- less than C => 1!/1! = 1
- less than A => 0

index = 30 + 0 + 0 + 2 + 1 + 0 = 33

"""

import itertools
import math


def multi_factorial(n: int, divisors: list[int]) -> int:
    """Returns the multi-factorial of n with divisors."""
    return math.factorial(n) // math.prod(math.factorial(d) for d in divisors)


def unique_permutations(sequence: list[int]) -> list[tuple[int, ...]]:
    """Returns permutations of a sequence with possible duplicates."""
    solutions = set()
    for perm in itertools.permutations(sequence):
        solutions.add(perm)
    return sorted(solutions)


def compute_permutation_index(sequence: list[int]) -> int:
    """Returns the index of a permutation of a sequence.

    Supports duplicates.
    """
    counts = [0] * len(set(sequence))
    for term in sequence:
        counts[term] += 1

    perm_number = 0
    n = len(sequence)
    for i, index in enumerate(sequence):
        for j in range(index):
            if counts[j] > 0:
                counts[j] -= 1
                perm_number += multi_factorial(n - i - 1, counts)
                counts[j] += 1
        if counts[index] > 0:
            counts[index] -= 1
    return perm_number


def index_to_permutation(index: int, counts: list[int]) -> tuple[int, ...]:
    """Returns the permutation of a sequence given its index.

    Supports duplicates.
    """
    n = sum(counts)
    permutation = []
    for i in range(n):
        for j in range(len(counts)):
            if counts[j] > 0:
                counts[j] -= 1
                n_perms = multi_factorial(n - i - 1, counts)
                if n_perms <= index:
                    index -= n_perms
                else:
                    permutation.append(j)
                    break
                counts[j] += 1
    return tuple(permutation)


def test() -> None:
    """Run test cases."""
    perms = unique_permutations([0, 0, 0, 1, 1, 2])
    for i, permutation in enumerate(perms):
        assert compute_permutation_index(list(permutation)) == i
        assert index_to_permutation(i, [3, 2, 1]) == permutation
