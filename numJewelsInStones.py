# https://leetcode.com/problems/jewels-and-stones/solution/

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        for s in stones:
            if s in jewels: 
                count += 1
        return count
      
      

 # Time: O(n*n)
 # Space: O(1)
    
    
   def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsSet = set(jewels)
        return sum(s in jewelsSet for s in stones)
    
    
    # Time: O(len(jewels) + len(stones))
    # Space: O(len(jewels)
    
    
    
    
      def numJewelsInStones(self, J, S):
        return sum(s in J for s in S)
    
    # Time: O(len(jewels) * len(stones)) 
    # Space: O(1) 
    
