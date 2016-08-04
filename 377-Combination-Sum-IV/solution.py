class Solution(object):
    def __init__(self):
        self.cnt=0
        
    def helper(self,nums,res,target):
        if res==target:
           self.cnt+=1
           return
        
        if res>target:
            return
        
        for num in nums:
            self.helper(nums,res+num,target)
            
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums:
            return 0
            
        if len(nums)==1 and nums[0]<target:
            return 0
            
        self.helper(nums,0,target)
        return self.cnt
        