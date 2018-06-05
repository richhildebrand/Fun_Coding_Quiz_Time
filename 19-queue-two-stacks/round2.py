class MyQueue(object):

    def __init__(self):
        self.in_queue = []
        self.out_queue = []

    def enqueue(self, item):
        self.in_queue.append(item)


    def dequeue(self):
        if len(self.out_queue) != 0: return self.out_queue.pop(), 0

        steps = 0
        while len(self.in_queue) > 1:
            steps += 1
            item = self.in_queue.pop()
            self.out_queue.append(item)

        return self.in_queue.pop(), steps

