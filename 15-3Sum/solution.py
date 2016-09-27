class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res,n=[],len(nums)
        nums.sort()
        for i in xrange(n-2):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                low,high,total=i+1,n-1,0-nums[i]
                while low<high:
                    if nums[low]+nums[high]==total:
                        res.append([nums[i],nums[low],nums[high]])
                        while low<high and nums[low]==nums[low+1]:
                            low+=1
                        while low<high and nums[high]==nums[high-1]:
                            high-=1
                        low+=1
                        high-=1
                    elif nums[low]+nums[high]>total:
                        high-=1
                    else:
                        low+=1
        return res
        
                