from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    furthest_reach, last = 0, len(A) - 1
    i = 0
    while i <= furthest_reach and furthest_reach < last:
        furthest_reach = max(furthest_reach, A[i] + i)
        i += 1
    return furthest_reach >= last


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
