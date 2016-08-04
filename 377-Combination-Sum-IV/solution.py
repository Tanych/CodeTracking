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
        dp=[0]*(target+1)
        dp[0]=1
        
        for i in xrange(1,len(dp)):
            for j in xrange(len(nums)):
                if i>=nums[j]:
                    dp[i]+=dp[i-nums[j]]
        return dp[target]
            