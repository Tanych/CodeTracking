class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not filter(lambda x:x==0, nums):
            return 0
        return sum(i for i in xrange(len(nums)+1))-sum(nums)