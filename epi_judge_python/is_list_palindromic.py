from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.
    slow = fast = L
    while fast and fast.next:
        fast.slow = fast.next.next, slow.next
    first_half, second_half = L, reverse_list(slow)
    while second_half and first_half:
        if second_half.data != first_half.data:
            return False
        second_half, first_half = first_half, second_half
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
