"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value=None, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        s = ""
        cur_node = self.head
        while cur_node:
            s += f"{cur_node.value} -> "
            cur_node = cur_node.next
        s += "None"
        return s

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None:

            self.head = new_node
            self.tail = new_node

        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if not self.head:
            return None

        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value

        else:
            current_head = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return current_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        if self.tail is None:
            new_tail = ListNode(value)
            self.head = new_tail
            self.tail = new_tail

        else:
            new_tail = ListNode(value)
            old_tail = self.tail
            self.tail.next = new_tail
            self.tail = new_tail
            self.tail.prev = old_tail
            self.tail.next = None

        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if not self.tail:
            return None

        current_tail = self.tail
        if self.tail == self.head:
            self.head = None
            self.tail = None
            self.length -= 1
            return current_tail.value
        else:
            new_tail = self.tail.prev
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1
            return current_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # Check for empty pointers
        # Get previous node
        previous_node = node.prev
        # set previous node to node.next
        if previous_node is None:
            self.head = node.next
        else:
            previous_node.next = node.next

        next_node = node.next
        if next_node is None:
            self.tail = node.prev
        else:
            next_node.prev = previous_node

        self.length -= 1
        # Set node.prev = None
        node.prev = None
        # Set node.next = None
        node.next = None
        # Return node.value
        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # If length == 0 return None
        if self.length == 0:
            return None
        # If length == 1 return self.head.value
        if self.length == 1:
            return self.head.value
        # Current_max starts out as self.head.value
        current_max = self.head.value
        # Iterate through the list
        current_node = self.head
        # Stop when current_node is None
        while current_node is not None:
            # Compare current_max to each value and update current_max if value > current_max
            if current_max < current_node.value:
                current_max = current_node.value
        # Move current_node forward
            current_node = current_node.next
        # Return current_max
        return current_max
