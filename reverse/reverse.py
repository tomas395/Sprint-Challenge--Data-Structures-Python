class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head is None:  # check to see if the head is populated first and if it isn't, return None
            return
        elif node.next_node:  # then if populated and has a next, recursivly move and swap the next node and nodes pointers
            self.reverse_list(node.next_node, node)
            node.next_node = prev
        else:  # change the pointer of next_node to the prev node and assign the self.head as the node
            self.head = node
            node.next_node = prev
