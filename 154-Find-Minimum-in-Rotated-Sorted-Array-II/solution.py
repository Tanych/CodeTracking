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
            # kick out the duplicate
            if nums[end]==vmid:
                end-=1
            elif nums[end]<vmid:
                start=mid
            else:
                end=mid
                # if all larger than vmid
                if nums[start]<=vmid:
                    return nums[start]
        return nums[start]