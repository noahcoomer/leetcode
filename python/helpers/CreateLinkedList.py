from obj.ListNode import ListNode

# Create a Linked List from an array of values
def CreateLinkedList(arr):
	n = len(arr)
	dummy = ListNode(0)
	curr = dummy
	for i in arr:
		curr.next = ListNode(i)
		curr = curr.next
	return dummy.next