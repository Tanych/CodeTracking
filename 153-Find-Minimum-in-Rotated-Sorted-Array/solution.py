class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # using two pointer to find the trends of array
        n=len(nums)
        # two pointer
        start,end=0,n-1
        # factor to compare
        last=nums[n-1]
        
        # finding the pivot
        while start+1<end:
            mid=start+(end-start)/2
            if nums[mid]<last:
                end=mid
            else:
                start=mid
        # decide which one is the answer
        if nums[start]>last:
            return nums[end]
        else:
            return nums[start]
        