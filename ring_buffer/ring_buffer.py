'''A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds the given element to the buffer. The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.
'''
from DLL import DoublyLinkedList
# in the DLL we created the functions `add_to_tail` and `remove_from_head` that might help??
class RingBuffer:
    def __init__(self, capacity):
        # set length
        self.capacity = capacity
        # initialize the buffer using a list
        self.storage = DoublyLinkedList()
        # set what node/item were starting with and then currently on
        self.current = None

    def append(self, item):
        # if the length of the list is less thn the capacity
        if self.storage.length < self.capacity:
            # add the item to the list
            self.storage.add_to_tail(item)
            # current becomes the head of the list
            self.current = self.storage.head
        # if the length of the list is at capacity
        elif self.storage.length == self.capacity:
            # store the current head the current head
            evicted = self.storage.head
            # remove the current head
            self.storage.remove_from_head()
            # add the item to the list
            self.storage.add_to_tail(item)
            # check to see if the removed head is the same as the curent node
            if evicted == self.current:
                # current becomes the tail
                self.current = self.storage.tail

    def get(self):
        # create a list to store the items
        rblist = []
        # if the DLL is empty
        if not self.storage.length:
            # return none
            return None
        # store the current item
        starter = self.current
        # add the current item to the list
        rblist.append(starter.value)
        # if there is a next node
        if starter.next:
            # then go to the next node
            s_next = starter.next
        # or start start at the head
        else:
            s_next = self.storage.head
        # as long as the item isnt the same as teh starting item
        while s_next is not starter:
            # add the item to the rblist
            rblist.append(s_next.value)
            # if there is a next value
            if s_next.next:
                # continue next
                s_next = s_next.next
            else:
                # go back to the next head
                s_next = self.storage.head
        # return the list
        return rblist