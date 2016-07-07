class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if i do all in naive:
        if target in nums:
            return nums.index(target)
        else:
            return -1