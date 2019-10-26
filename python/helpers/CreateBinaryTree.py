from obj.TreeNode import TreeNode

# Create a Binary Tree given a list of values
def CreateBinaryTree(arr):
    n = len(arr)
    if n == 0:
        return None
    
    root = TreeNode(arr[0])
    visited = [root]

    for i in range(1, n):
        if arr[i] != None:
            node = TreeNode(arr[i])
            visited.append(node)
            index = (i - 1) // 2 
            if i % 2 != 0:
                visited[index].left = node
            else:
                visited[index].right = node
        else:
            visited.append(None)
    return root