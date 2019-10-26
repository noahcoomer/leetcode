# 10/25/2019
# 104. Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from helpers.CreateBinaryTree import CreateBinaryTree

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = [root]
        depth = 0

        while queue:
            depth += 1
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        
        return depth


if __name__ == '__main__':
    case = [3, 9, 20, None, None, 15, 7]
    root = CreateBinaryTree(case)

    solution = Solution()
    answer = solution.maxDepth(root)
    print(answer)
