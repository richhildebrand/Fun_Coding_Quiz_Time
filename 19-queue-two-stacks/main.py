class MyQueue():

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        steps = 0
        if len(self.out_stack) != 0: return (self.out_stack.pop(), steps)

        while len(self.in_stack):
            steps += 1

            item = self.in_stack.pop()
            self.out_stack.append(item)

        first_item = self.out_stack.pop()
        return (first_item, steps)
    