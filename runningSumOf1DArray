# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res = []
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            # print(nums)
        return nums
      
  # Time: O(n)
  # Space: O(1)
