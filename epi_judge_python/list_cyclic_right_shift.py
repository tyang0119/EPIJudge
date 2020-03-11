from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    if L is None:
        return L

    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next

    k %= n
    if k == 0:
        return L

    tail.next = L
    step, new_tail = n - k, tail
    while step:
        step -= 1
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
