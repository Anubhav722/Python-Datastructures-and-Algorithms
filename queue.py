# Queue follows FIFO (First In First Out)
# The added first is called the front and the item added last is termed rear.
# Items can only added from the rear and removed from the front.
# The process of adding items to queue is enqueue.
# The process of removing items from the queue is termed dequeue.

class Queue(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		"""
		Assuming the rear is at the 0th index of the list.
		"""
		self.items.insert(0, item)

	def dequeue(self):
		"""
		The front is the element of the list.
		"""
		return self.items.pop()

	def size(self):
		return len(self.items)