# A collection of nodes that collectively form a sequence.
# Each node stores a reference to an object that is an element of the sequence,
# as well as a reference to the next node of the list.
# First and last nodes are known as the head of linked list.
# We can identify the tail as the node having None as its next reference.
# Each node references it's element and the next node.


# Inserting an element at the head of the linked list.
# Important property of the linked list is that it does not have a predetermined fixed size.
# It uses space proportionally to its current number of elements.

# To create a new node at the head of the list
# * We create a new node.
# * Set it's element to the new element.
# * Set it's next link to refer to the current head.
# * Then set the list's head to point to the new node.

# Inseting an element at the tail of the Singly linked list.
# * Create a new node.
# * Assign it's nxt reference to None.
# * Set the next reference of the tail to point to this new node.
# * Then update the tail reference itself to this new node.


# Removing an element from the head of the Singly linked list.
# * Pretty simple.

# Removing an element from the tail of the singly linked list.
# * Refer doubly linked list for such purposes.

class Node(object):

	def __init__(self, value):      # Simple Implementaion
		self.value = value			# a = Node(1), b = Node(2), c = Node(3)
		self.nextnode = None		# a.nextnode = b, b.nextnode = c
									# a.value
									# 1
									# a.nextnode.value
									# 2



# PROS OF LINKED LISTS:
# * They have constant time insertions and deletion. In comparison arrays will always require O(N)
# to do the same thing.
# * Linked list can continue to expand without having to specify their size.

# CONS OF LINKED LISTS:
# * To access an element in linked list. i.e. To access the Kth element, it takes O(k) time to reach
# from head to Kth element of the linked list whereas arrays have constant time operation.