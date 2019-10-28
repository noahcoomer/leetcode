# 10/28/2019
# Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

from helpers.CreateLinkedList import CreateLinkedList

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

if __name__ == '__main__':
    solution = Solution()

    cases = (
        [1, 2, 3, 4, 5],
        [1]
    )

    for case in cases:
        node = CreateLinkedList(case)
        answer = solution.reverseList(node)
        print(answer)
