class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        n=len(nums)
        if n==1:
            return 1
        
        minnum=min(nums)
        idx=nums.index(minnum)
        res=1
        tmin=-1<<32
        while idx<n-1:
            tmin=min(nums[idx+1:])
            if tmin>minnum:
                res+=1
                idx=nums.index(tmin)
            else:
                break
            
            
        return res
                
            