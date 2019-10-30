# 10/28/2019
# Symmetric Tree - https://leetcode.com/problems/symmetric-tree/

from helpers.CreateBinaryTree import CreateBinaryTree
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recursive(root):
            def recurse(left, right):
                if not left and not right:
                    return True
                if not left or not right:
                    return False
                return left.val == right.val and recurse(left.left, right.right) and recurse(left.right, right.left)

            if not root:
                return True
            return recurse(root, root)
        
        def iterative(root):
            if not root:
                return True
            level = []
            queue = deque([root])
            while queue:
                n = len(queue)
                for _ in range(n):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                        level.append(node.left.val)
                    else:
                        level.append(None)
                    if node.right:
                        queue.append(node.right)
                        level.append(node.right.val)
                    else:
                        level.append(None)
                m = len(level)
                first = level[:m//2]
                last = level[m//2:]
                if first != last[::-1]:
                    return False
                level = []
            return True
            
        return recursive(root)
    

if __name__ == '__main__':
    solution = Solution()

    cases = (
        [1,2,2,3,4,4,3],
        [1,2,2,None,3,None,3],
        [],
        [1]
    )

    for case in cases:
        print(case)
        root = CreateBinaryTree(case)
        answer = solution.isSymmetric(root)
        print(answer)
        