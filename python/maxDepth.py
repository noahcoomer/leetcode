# 10/25/2019
# 104. Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import deque, popleft from collections

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = [(root, 1)]
        max_depth = 0
        
        while queue:
            for node, depth in queue:
                max_depth = max(max_depth, depth)
                if node.left:
                    new_queue.append((node.left, depth + 1))
                if node.right:
                    new_queue.append((node.right, depth + 1))
            
        return max_depth