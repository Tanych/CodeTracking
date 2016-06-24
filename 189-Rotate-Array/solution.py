class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # the efficient way to using reverse
        # [1,2,...k,k+1,...n]--->k,[n-k,n-k-1,...0,n,n-1...n-k+1]-->[n-k+1,n-k+2...n-1,n,0,...n-k-1,n-k]
        if k<=0:
            return
        n=len(nums)
        k, end = k % n, n-1
        self.reverse(nums,0, end-k)
        self.reverse(nums,end-k+1,end)
        self.reverse(nums,0,end)
        
    def reverse(self,nums,start,end):
        while start<end:
            # swap
            nums[start],nums[end]=nums[end],nums[start]
            # cotinue
            start+=1
            end-=1