from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == len(self.storage):
            self.current.value = item

            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)
            if len(self.storage) == 1:
                self.current = self.storage.head

    def get(self):
        buffer_contents = []

        node = self.storage.head
        while node is not None:
            buffer_contents.append(node.value)
            node = node.next

        return buffer_contents
