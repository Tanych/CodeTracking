class Solution(object):
    def twoSumSmaller(self, nums, start, target):
        total=0
        left,right=start,len(nums)-1
        while left<right:
            if nums[left]+nums[right]<target:
               total+=right-left
               left+=1
            else:
                right-=1
        return total
        
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        if n<3: return 0
        nums.sort()
        total=0
        for i in xrange(n-2):
            total+=self.twoSumSmaller(nums,i+1,target-nums[i])
        return total