class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.max_numbers_in_stack = []

    def get_max(self):
        items_in_stack = len(self.max_numbers_in_stack)
        if items_in_stack == 0: return None
        return self.max_numbers_in_stack[items_in_stack -1]

    def push(self, item):
        max_number = self.get_max()
        if not max_number or max_number < item:
            self.max_numbers_in_stack.append(item)

        Stack.push(self, item)

    def pop(self):
        item = Stack.pop(self)

        max_number = self.get_max()
        if item == max_number: self.max_numbers_in_stack.pop()

        return item
