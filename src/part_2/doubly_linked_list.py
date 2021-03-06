# Each ListNode holds a reference to its previous node as well as its next node in the List.
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    # Wrap the given value in a ListNode and insert it after this node. Note that this node could already have a next node it is point to.
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    # Wrap the given value in a ListNode and insert it before this node. Note that this node could already have a previous node it is point to.
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    # Rearranges this ListNode's previous and next pointers accordingly, effectively deleting this ListNode.
    def delete(self):
        if self.prev:
            self.prev.next = self.next
            # point the previous node's next "arrow" at whatever was next to the deleted node
        if self.next:
            # point the next node's prev "arrow" at whatever was previous to the deleted node
            self.next.prev = self.prev


# Our doubly-linked list class. It holds references to the list's head and tail nodes.
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    # Removes a node from the list and handles cases where the node was the head or the tail
    def delete(self, node):
        # the list is empty, do nothing
        if self.head is None and self.tail is None:
            return
        # subtract 1 from length
        self.length -= 1
        # the list is only one node
        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
        # the node is the HEAD node
        elif self.head == node:
            self.head = node.next
            node.delete()
        # the node is the TAIL node
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        # the node is just some node in the list
        else:
            node.delete()

    # Wraps the given value in a ListNode and inserts it as the new head of the list. Don't forget to handle the old head node's previous pointer accordingly.

    def add_to_head(self, value):
        # create new node (don't actually need the 'None, None')
        new_node = ListNode(value, None, None)
        self.length += 1
        # if list if currently empty, add node
        if self.head is None and self.tail is None:
            # set the head and tail to equal the new node
            self.head = new_node
            self.tail = new_node
        # if list already has elements in it, add to the front
        else:
            # make new node's next value point to current head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Removes the List's current head node, making the current head's next node the new head of the List. Returns the value of the removed Node.

    def remove_from_head(self):
        if self.head is None:
            return None
        head_value = self.head.value
        self.delete(self.head)
        return head_value

    # Wraps the given value in a ListNode and inserts it as the new tail of the list. Don't forget to handle the old tail node's next pointer accordingly.
    def add_to_tail(self, value):
        # if list is empty, set head and tail to new node
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        # if list isn't empty, insert after tail
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    # Removes the List's current tail node, making the current tail's previous node the new tail of the List. Returns the value of the removed Node.
    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value

    # Removes the input node from its current spot in the List and inserts it as the new head node of the List.
    def move_to_front(self, node):
        if node is self.head:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_head(old_value)

    # Removes the input node from its current spot in the List and inserts it as the new tail node of the List.
    def move_to_end(self, node):
        if node is self.tail:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_tail(old_value)

    # Returns the highest value currently in the list
    def get_max(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list has only one element, return that value
        if self.length == 1:
            return self.head.value
        # else, loop through the list, comparing each value to the current largest value
        current_node = self.head
        largest = 0
        while current_node is not None:
            if current_node.value > largest:
                largest = current_node.value
            current_node = current_node.next
        return largest
