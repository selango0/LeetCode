'''
Implement search in BST.

      
              10
              /\
            5   15
           /\      \
         3   7     18
         
     [10, 5, 3]
     Time complexity: O(h) - n = 2^h -> log2(n) = h
     Memory complexity: O(h) - h height of tree
     
                0               Level: 0 | Nodes: 1
              /   \
            0      0            Level: 1 | Nodes: 2 | Total: 3
           / \    /  \
          0   0  0    0         Level: 2 | Nodes: 4 | Total: 7
                                Level: 3 | Nodes: 8 | Total: 15
                                Level: 4 | Nodes: 16| Total: 31
          
          Level: h | Nodes: f(h) = 2^h
          For a perfect BST with h levels we have 2^(h+1)-1 nodes
          
          n = 2^h -> log2(n) = h
'''

def searchBST(root, key):
    if root is None:
        return False
    if root.val == key:
        return True
    elif root.val < key:
        return searchBST(root.right, key)
    else:
        return searchBST(root.left, key)

# create TreeNode
root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))

print(searchBST(root, 15)) # should print True
print(searchBST(root, 8)) # should print False
