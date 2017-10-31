# Each node keeps an explicit reference to the node to the node before it and a reference to the
# node after it.
# Allow a greater variety of constant/O(1)-time update operations, including insertions and deletions.
# Use the term "next" for the reference to the node that follows another.
# Use the term "prev" for the reference to the node that preceeds it.
# A "header" node is at the beginning of the list.
# A "trailer" node is at the end of the list
# These "dummy" nodes are known as "sentinels".

# Inserting and deleting with a Doubly Linked List.
# Every insertion into doubly linked list representation will take place between a pair of existing
# nodes.
# When a new element is inserted at the front of the sequence, we will simply add the new node
# between the header and the node that is currently after the header.

# IMPLEMENTATION

class DoublyLinkedListNode(object):

	def __init__(self, value):				# a = DoublyLinkedListNode(1)
		self.value = value					# b = DoublyLinkedListNode(2)
		self.next_node = None 				# c = DoublyLinkedListNode(3)
		self.prev_node = None 				
											# a.next_node = b
											# b.prev_node = a
											# b.next_node = c
											# c.prev_node = b
