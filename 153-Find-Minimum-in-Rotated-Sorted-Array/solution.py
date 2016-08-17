class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if not n:
            return -1
        start,end=0,n-1

        while start<end:
            mid=start+(end-start)/2
            vmid=nums[mid]
            if nums[end]<vmid:
                start=mid+1
            else:
                end=mid
                # if all less than vmid
                if nums[start]<=vmid:
                    return nums[start]
        return nums[start]