class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if can use sort
        nums.sort()
        return nums[len(nums)/2]