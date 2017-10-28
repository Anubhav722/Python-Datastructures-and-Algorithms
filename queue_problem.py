# Using two stacks implement a queue

class Queue2Stacks(object):

    def __init__(self):
        
        # Given two stacks
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        # Fill out the code here
        self.instack.append(element)

    def dequeue(self):
        # Fill out the code here.
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()