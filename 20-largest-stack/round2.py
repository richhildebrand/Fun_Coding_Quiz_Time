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
        self.maxes = []
        super().__init__()

    def get_max(self):
        if len(self.maxes) == 0: return None
        return self.maxes[len(self.maxes)-1]

    def push(self, item):
        if len(self.maxes) == 0 \
        or self.get_max() <= item:
            self.maxes.append(item)

        super().push(item)
    
    def pop(self):
        item = super().pop()
        if item == self.get_max(): self.maxes.pop()

        return item