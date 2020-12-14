
class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None


def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    # Set right pointer at n nodes away from head
    for i in range(n - 1):

        # Check for edge case of not having enough nodes!
        if not right_pointer.next_node:
            raise LookupError('Error: n is larger than the linked list.')

        # Otherwise, we can set the block
        right_pointer = right_pointer.next_node

    # Move the block down the linked list
    while right_pointer.next_node:
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node

    # Now return left pointer, its at the nth to last element!
    return left_pointer


"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e


####

class TestNLast(object):

    def test(self, sol):
        assert_equal(sol(2, a), d)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestNLast()
t.test(nth_to_last_node)












