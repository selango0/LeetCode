

# https://leetcode.com/problems/number-of-good-pairs/


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if(nums[i] == nums[j])  and i<j:
                    res.append([i,j])
        return len(res)
    
    
# Time: O(n^2) 
# Space: O(1)? 
