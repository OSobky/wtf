"""
This script solves the problem 1480. Running Sum of 1d Array in LeetCode 
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # get the sum for each element in the running array
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums