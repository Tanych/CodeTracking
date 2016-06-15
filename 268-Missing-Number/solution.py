class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(i for i in xrange(len(nums)+1))-sum(nums)