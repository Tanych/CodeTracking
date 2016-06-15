class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ret=[1]*n
      
        
        # record the previous product result
        preprod=1
        # the left part
        for i in xrange(1,n):
            preprod=preprod*nums[i-1]
            ret[i]*=preprod
        
        preprod=1
        # the right part
        for i in xrange(n-2,-1,-1):
            preprod=preprod*nums[i+1]
            ret[i]*=preprod

        return ret