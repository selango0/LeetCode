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
