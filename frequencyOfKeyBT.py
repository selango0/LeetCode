# Write a recursive function that returns the frequency of a key given as input in a Binary Tree
# Definition for a binary tree node.
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
         
     Time complexity: O(n) we are traversing each node once for n = # of nodes
     Memory complexity: O(h) h = max height of tree
'''


def getFrequency(root, key):
    freq = 0
    if root is None:
        return 0
    if root.val == key:
        freq += 1
    left = getFrequency(root.left, key)
    right = getFrequency(root.right, key)
    return left + right + freq

root = TreeNode(5, TreeNode(5), TreeNode(6))
print(getFrequency(root, 5)) # should give 2
print(getFrequency(root, 6)) # should give 1
print(getFrequency(root, 3)) # should give 0
