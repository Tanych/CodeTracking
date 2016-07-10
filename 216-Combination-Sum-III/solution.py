class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        digits=[1,2,3,4,5,6,7,8,9]
        
        def dfs(nums,target,path,res,level,step):
            """
            level: to record the recursive level and all possible
            step: record the elements of the results
            path: one result of the recursive
            """
            if step==k and target==0:
                res.append(path)
                return
            
            if step>k or target<0:
                return
            
            for i in xrange(level,len(nums)):
                if nums[i]<=target:
                    dfs(nums[:i]+nums[i+1:],target-nums[i],path+[nums[i]],res,i,step+1)
        res=[]
        dfs(digits,n,[],res,0,0)
        return res
        