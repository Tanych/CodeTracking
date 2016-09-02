class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if lower>upper:
            return []
            
        if not nums:
            if upper==lower:
                return [str(lower)]
            else:
                return [str(lower)+'->'+str(upper)]
        
        res=[]
        if nums[0]-lower==1:
            res.append(str(lower))
        elif nums[0]-lower>=2:
            res.append(str(lower)+'->'+str(nums[0]-1))
            
        for i in xrange(1,len(nums)):
            if nums[i]-nums[i-1]==2:
                res.append(str(nums[i-1]+1))
            elif nums[i]-nums[i-1]>2:
                res.append(str(nums[i-1]+1)+'->'+str(nums[i]-1))
        
        if upper-nums[-1]==1:
            res.append(str(upper))
        elif upper-nums[-1]>=2:
            res.append(str(nums[-1]+1)+'->'+str(upper))
        return res
        