from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)

        else:

            if not self.right:
                self.right = BinarySearchTree(value)

            else:
                return self.right.insert(value)

    def contains(self, target):

        if target == self.value:
            return True

        else:
            if target < self.value:
                if not self.left:
                    return False
                return self.left.contains(target)
            else:
                if not self.right:
                    return False
                return self.right.contains(target)

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):

        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        if node.right:
            print(node.value)
            node.right.in_order_print(node.right)
        else:
            print(node.value)

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.size > 0:
            popped = queue.dequeue()
            print(popped.value)

            if popped:
                if popped.left:
                    queue.enqueue(popped.left)
                if popped.right:
                    queue.enqueue(popped.right)

    def dft_print(self, node):
        stack = Stack()

        stack.push(node)

        while stack.size > 0:
            popped = stack.pop()
            print(popped.value)

            if popped:
                if popped.left:
                    stack.push(popped.left)

                if popped.right:
                    stack.push(popped.right)
