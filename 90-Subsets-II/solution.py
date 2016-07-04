class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    
        def dfs(nums,idx,path,res):
            c=nums[idx]
            res.append([c] + path)
            for i in xrange(idx-1,-1,-1):
                if i<idx-1 and nums[i]==nums[i+1]:
                    continue
                dfs(nums,i,[c]+path,res)

        res=[]
        n=len(nums)
        nums.sort()
        for i in xrange(n):
            if i<n-1 and nums[i]==nums[i + 1]:
                continue
            dfs(nums, i, [], res)
        res.append([])
        return res