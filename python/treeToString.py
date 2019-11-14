# 11/14/19
# Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from helpers.CreateBinaryTree import CreateBinaryTree

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        ans = self.recurse(t)
        return ans[1:-1]
    
    def recurse(self, node):
        if not node:
            return ""
        if not node.left and node.right:
            return "(" + str(node.val) + "()" + self.recurse(node.right) + ")"
        else:
            return "(" + str(node.val) + self.recurse(node.left) + self.recurse(node.right) + ")"


if __name__ == '__main__':
    solution = Solution()

    cases = (
        [1,2,3,4], # => 1(2(4))(3)
        [1,2,3,None,4], # => 1(2()(4))(3)
    )

    for case in cases:
        root = CreateBinaryTree(case)
        answer = solution.tree2str(root)
        print(answer)
