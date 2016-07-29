class Solution(object):
    def partion(self, nums):
        pivot=nums[0]
        n=len(nums)
        
        i,j=0,n-1
        while i<j:
            while i<n and nums[i]<=pivot:
                i+=1
            while j>=0 and nums[j]>pivot:
                j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        # swap the first element
        nums[j],nums[0]=nums[0],nums[j]
        return j
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        r=self.partion(nums)
        if n-r>k:
            return self.findKthLargest(nums[r+1:],k)
        elif n-r<k:
            return self.findKthLargest(nums[:r],k-(n-r))
        elif n-r==k:
            return nums[r]
            
        