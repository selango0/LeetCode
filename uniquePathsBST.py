# To find the number of unique paths from a the root til the end of the BST


# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
         5
        / \
       5   6
       /\  /\
      N  N N N
      
              10
              /\
            5   15
           /\      \
         3   7     18
         '''
# Time: O(n) -  n = number of nodes 
# Memory: O(h) h = height of tree

def uniquePaths(root):
    # base case 1
    if root is None:
        return 0
    # base case 2
    if root.left is None and root.right is None:
        return 1
    # recursive case 
    left = uniquePaths(root.left)
    right = uniquePaths(root.right)
    return left + right
    
   #  return root.left + root.right
    
    

root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
print(uniquePaths(root))
