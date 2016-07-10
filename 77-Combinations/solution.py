class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        digits=[]
        for i in xrange(1,n+1):
            digits.append(i)
        
        def dfs(nums,path,res,level,step):
            print level,k
            if step==k:
                res.append(path)
                return
            
            if step>k:
                return
            for i in xrange(level,len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[nums[i]],res,i,step+1)
        res=[]
        dfs(digits,[],res,0,0)
        return res