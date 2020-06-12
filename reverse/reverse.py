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
    ## DONE ITERATIVELY
    def reverse_list(self, node, prev):
        # initilize prev as none
        prev = None
        # initialize node as the head node
        node = self.head
        # make sure the node is not none
        while node is not None:
            # store the next node
            n_node = node.next_node
            # set the next node to the prev node
            node.next_node = prev
            # set the prev node to the node itself
            prev = node
            # set the node to the next node
            node = n_node
        # set the head to the prev node
        self.head = prev

    ## TRYING WITH RECURSION
    # def reverse_list(self, node, prev):
    #     # if the list is empty or there is only one node in the list
    #     if node.get_next() == None:
    #         # set the head to node
    #         self.head = node
    #         # return
    #         return
    #     self.reverse_list(node.get_next(), None)
    #     newcurr = node.get_next()
    #     newcurr.set_next(node)
    #     node.set_next(None)
        