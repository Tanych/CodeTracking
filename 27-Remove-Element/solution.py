class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if n==0 :
            return 0
        if n==1:
            if nums[0]==val:
                return 0
            else:
                return 1
            
        p=0
        q= n-1
        while p<q:
            while p<=n-1 and nums[p]!=val:
                p+=1
            while q>=0 and nums[q]==val:
                q-=1
            # swap
            if p<q:
                nums[p],nums[q]=nums[q],nums[p]
                q-=1
        return q+1