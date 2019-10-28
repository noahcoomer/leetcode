# 10/28/2019
# Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from obj.ListNode import ListNode
from helpers.CreateLinkedList import CreateLinkedList

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        for i in range(n + 1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next

if __name__ == '__main__':
	solution = Solution()

	cases = (
		([1, 2, 3, 4, 5], 2),
		([1], 1),
		([1, 2, 3], 3)
	)

	for arr, n in cases:
		node = CreateLinkedList(arr)
		answer = solution.removeNthFromEnd(node, n)
		print(answer)