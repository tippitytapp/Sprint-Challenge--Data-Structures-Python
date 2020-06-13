"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BSTNode:
    def __init__(self, value = None):
        self.root = None
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else: 
                self.right = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else: 
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def _recur_contains(self, target):
        # base case?
        # we find the target in a tree node
        if self.value == target:
            return True
        # figure out which direction we need to go in
        if target < self.value:
            # we go left
            if not self.left:
                return False
            else:
                return self.left._recur_contains(target)
        # or, we get to a spot where the node should be, but nothing is there
        # how do we move towards the base case?
        else:
            if not self.right:
                return False
            else:
                return self.right._recur_contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # we can keep going right until we cant go right anymore

        if self.right:
            return self.right.get_max()
        else:
            return self.value

        ## THIS IS HOW SEAN DID IT ##
        # if not self.right:
        #     return self.value
        # return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # this doesnt actually return anything
        #needs to call the fn on self.value
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

        ## THIS IS HOW SEAN DID IT ##
        # fn(self.value)
        # we do we propagate to all the other nodes in the tree
        # is there a left child?
        # if self.left:
            # if yes, then call its for_each with the same fn
            # self.left.for_each(fn)
        # is there a right child?
        # if self.right:
            # if yes, then call its for_each with the same fn
            # self.right.for_each(fn)
    
    def iter_depth_for_each(self, fn):
        # with depth-first traveral, theres a certain order to when we visit nodes
        # whats tht order?
        # init a stack to work for our LIFO order
        stack = []
        # add the first node to our stack
        stack.append(self)
        # continue traversing until our stack is empty
        while len(stack) > 0:
            # pop off the stack
            cur_node = stack.pop()
            # add its children to the stack
            # add right child first, and left side second to ensure left is popped off the stack first
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
            # call the fn on its children
            fn(self.value)
    
    def iter_bredth_for_each(self, fn):
        q = deque()
        q.append(self)
        while len(q) > 0:
            cur_node = q.popleft()
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            fn(self.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # self.root = node
        if node:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # pass
        visited = []
        if node:
            visited.append(node)
            print(node.value)
        current = node
        while current:
            if current.left:
                print(current.left.value)
                visited.append(current.left)
            if current.right:
                print(current.right.value)
                visited.append(current.right)
            visited.pop(0)
            if not visited:
                break
            current = visited[0]
                # current = node
                # queue = deque()
                # while queue or current:
                #     if current:
                #         queue.push(current)
                #         current = current.left
                #     else:
                #         current = queue.pop()
                #         print(current.value, end="\n")
                #         current = current.right
                # print()
                # queue = []
                # queue.append(node.value)
                # while(len(queue) > 0):
                #     node = queue.pop(0)
                #     print(node)
                #     if self.left is not None:
                #         queue.append(self.left)
                #     if self.right is not None:
                #         queue.append(self.right)
                

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # pass
        # node = BSTNode(traversal_type)
        visited = []
        visited.append(node)
        while len(visited) > 0:
            node = visited.pop()
            print(node.value)
            if node.left:
                visited.append(node.left)
            if node.right:
                visited.append(node.right)



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        print(node.value)
        node.pre_order_dft(node.left)
        node.pre_order_dft(node.right)



    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # pass
        if node is None:
            return
        node.post_order_dft(node.left)
        node.post_order_dft(node.right)
        print(node.value)