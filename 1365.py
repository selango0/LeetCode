# How Many Numbers Are Smaller Than the Current Number https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution(object):
    # Brute Force
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
    
    # Dict 
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
	temp = sorted(nums)
	mapping = {}
	result = []
	for i in range(len(temp)):
		if temp[i] not in mapping:
			mapping[temp[i]] = i
	for i in range(len(nums)):
		result.append(mapping[nums[i]])
	return result

   # Time: O(nlogn) bc sorting
   # Space: O(n) using dict
    
