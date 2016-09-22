class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res,n,i=[],len(nums),0
        i=0 
        while i<n:
            s=str(nums[i])
            j=i+1
            while j<n and nums[j]==nums[j-1]+1:
                j+=1
            if j!=i+1:
                res.append(s+'->'+str(nums[j-1]))
            else:
                res.append(s)
            i=j
        return res
        