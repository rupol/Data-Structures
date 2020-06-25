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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare to the new value we want to insert

        # if new value is smaller, insert to the left
        if value < self.value:
            # set the left child to the new node with the new value
            if self.left is None:
                self.left = BSTNode(value)
            # if self.left is already taken by a node
            else:
                # make that node call insert
                self.left.insert(value)

        # if new value is larger, insert to the right
        if value >= self.value:
            # set the right child to the new node with the new value
            if self.right is None:
                self.right = BSTNode(value)
            # if self.right is already taken by a node
            else:
                # make that node call insert
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target is equal to the root
        if self.value == target:
            return True
        if target <= self.value:
            # check left subtree
            # if you can't go left, return false
            if self.left is None:
                return False
            # if there's a node, make that node call contains
            return self.left.contains(target)
        if target > self.value:
            # check right subtree
            # if you can't go right, return false
            if self.right is None:
                return False
            # if there's a node, make that node call contains
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, let's find the largest number there by calling get_max on the right subtree
        # if we can't go right, return the current value
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        # if you can go left, call for_each on the left tree
        if self.left:
            self.left.for_each(fn)

        # call the function on the value
        fn(self.value)

        # if you can go right, call for_each on the right tree
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node, in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # create a queue for nodes
        # add the first node to the queue
        # while queue is not empty
        # remove the first node from the queue
        # print the removed node
        # add all children into the queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # create a stack for nodes
        # add the first node to the stack
        # while the stack is not empty
        # remove the current node from the top of the stack
        # print that node
        # add all children to the stack (remember, order matters here - whatever you add first will be last processed)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# print_node = (x) => {console.log(x)}
def print_node(x): return print(x)


root_node = BSTNode(8)
root_node.insert(3)
root_node.insert(10)
root_node.insert(9)
root_node.insert(12)

root_node.for_each(print_node)
