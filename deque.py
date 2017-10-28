# Deque also has front and rear ends.
# The important thing to note is that items can be added and removed from both ends.
# It does not follow either LIFO or FIFO priniples.

class Deque(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def addFront(self, item):
		self.items.append(item)

	def removeFront(self):
		return self.items.pop()

	def addRear(self, item):
		self.items.insert(0, item)

	def removeRear(self):
		return self.items.pop(0)