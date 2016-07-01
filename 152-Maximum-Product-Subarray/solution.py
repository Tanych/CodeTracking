class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cur_max=cur_min=ret=nums[0]
        
        for i in xrange(1,len(nums)):
            if nums[i]<0:
                cur_max,cur_min=cur_min,cur_max
            cur_max=max(cur_max*nums[i],nums[i])
            cur_min=min(cur_min*nums[i],nums[i])
            ret=max(ret,cur_max)
        return ret