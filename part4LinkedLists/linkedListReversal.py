
class Node(object):

    def __init__(self, value):

        self.value = value
        self.next_node = Node


def reverse(head):

    # Set up current, previous, and next nodes
    current = head
    previous = Node
    next_node = Node

    # until we have gone through to the end of the list
    while current:

        # Make sure to copy the current nodes next node to a variable next_node
        # Before overwriting as the previous node for reversal
        next_node = current.next_node

        # Reverse the pointer to the next_node
        current.next_node = previous

        # Go one forward in the list
        previous = current
        current = next_node

    return previous





