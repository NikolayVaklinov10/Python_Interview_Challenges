
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









