# 10/30/2019
# Binary Tree Level Order Traversal

from helpers.CreateBinaryTree import CreateBinaryTree
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
          return []

        queue = deque([root])
        order = [[root.val]]

        while queue:
          new_queue = []
          new_vals = []
          while queue:
            node = queue.popleft()
            if node.left:
              new_queue.append(node.left)
              new_vals.append(node.left.val)
            if node.right:
              new_queue.append(node.right)
              new_vals.append(node.right.val)
          
          if new_vals:
            order.append(new_vals)
          
          if new_queue:
            queue = deque(new_queue)
        
        return order
        

if __name__ == '__main__':
  solution = Solution()

  cases = (
    [3,9,20,None,None,15,7], # = [[3],[9,20],[15,7]]
    [1,2,3,4,5,6,7]
  ) 

  for case in cases:
    print(case)
    node = CreateBinaryTree(case)
    answer = solution.levelOrder(node)
    print(answer)       