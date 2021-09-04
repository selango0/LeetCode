# How Many Numbers Are Smaller Than the Current Number https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        ans = []
        for i, item in enumerate(nums):
            for j, jtem in enumerate(nums):
                if i != j and nums[j] < nums[i]:
                    count += 1
            ans.append(count)
            count = 0
        return ans
        
   # Time: O(n^2)
   # Space: O(1)
