class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in xrange(len(nums)):
            ret.append(reduce(lambda x, y: x * y, nums[:i]+nums[i+1:]))
        return ret