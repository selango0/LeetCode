# https://leetcode.com/problems/range-sum-of-bst/solution/


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        stack = [root]
        while stack: 
            current = stack.pop()
            if current:
                if low <= current.val <= high:
                    res += current.val 
                if low < current.val: 
                    stack.append(current.left)
                if high > current.val: 
                    stack.append(current.right)        
        return res
      
      
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(curr):            
            if curr:
                if low <= curr.val <= high: 
                    self.ans += curr.val
                if low < curr.val: 
                    dfs(curr.left)
                if high > curr.val:
                    dfs(curr.right)
        self.ans = 0
        dfs(root)
        return self.ans

      
 # Time: O(n) depends on # of nodes
 # Space: O(n) using stack size of n nodes 
