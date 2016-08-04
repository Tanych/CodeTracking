class Solution(object):
    def __init__(self):
        self.cnt=0
        
    def helper(self,nums,target,mapping):
        if mapping[target]!=-1:
            return mapping[target]
        res=0
        for num in nums:
            if target>=num:
                res+=self.helper(nums,target-num,mapping)
        mapping[target]=res
        return res
            
    def combinationSum4_up(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mapping=[-1]*(target+1)
        mapping[0]=1
        self.helper(nums,target,mapping)
        return mapping[target]
    
    def combinationSum4(self, nums, target):
        # for negative num, it makes the result be infinite
        # EX.[1,-1,2], 1,-1 can be 0, we can add bunches of couple of 0.
        dp=[1]+[0]*target
        
        for i in xrange(1,len(dp)):
            for j in xrange(len(nums)):
                if i>=nums[j]:
                    dp[i]+=dp[i-nums[j]]
        return dp[target]
            