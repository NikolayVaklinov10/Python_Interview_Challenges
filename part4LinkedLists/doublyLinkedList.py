
class DoublyLinkedListNode(object):

    def __init__(self, value):

        self.value = value
        self.next_node = None
        self.prev_node = None




a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b

print("The next value after B is: " + str(b.next_node.value))
print("The previous value before B is: " + str(b.prev_node.value))
print("The B value is: " + str(b.value))


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None

        # cycle challenge
def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True
    return False

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a  # Cycle Here!

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)

        print("ALL TEST CASES PASSED")



# Run Tests

t = TestCycleCheck()
t.test(cycle_check)






