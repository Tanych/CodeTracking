class Solution(object):
   def searchInsert(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length=len(nums)
        l=0
        r=length-1
        while l<=r:
            if l==r:
                return l if nums[l]>=target else l+1
            mid=(l+r)/2
            if nums[mid]>=target:
                r=mid
            else:
                l=mid+1
