import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    # TODO - you fill in here.
    def find_length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    l0_len, l1_len = find_length(l0), find_length(l1)
    if l0_len > l1_len:
        l0, l1 = l1, l0

    for _ in range(abs(l1_len - l0_len)):
        l1 = l1.next

    while l1 and l0 and l0 is not l1:
        l0, l1 = l0.next, l1.next
    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
