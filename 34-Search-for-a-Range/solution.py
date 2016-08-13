class Solution(object):
    def binarysearch(self,nums,target):
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)/2
            if nums[mid]>=target:
                r=mid
            else:
                l=mid+1
        return l
            
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        start=self.binarysearch(nums,target)
        # if use target==nums[start], it would occur error if[2,2] find 3,
        # out of range
        if target in nums[start:start+1]:
            # find the first pos that equal or larger than target
            end=self.binarysearch(nums,target+1)-1
            return [start,end]
        else:
            return [-1,-1]