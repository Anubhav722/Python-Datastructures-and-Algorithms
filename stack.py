# Stack follows LIFO (Last In First Out). The first element is called base and last is called top.
# Addition and removal of the elements happens from the top.
 # you can access any element in an array--not 
 # true for a stack, since you can only deal with the element at its top.
 # Further details here: 
 # https://softwareengineering.stackexchange.com/questions/147645/what-is-the-difference-between-an-array-and-a-stack

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)