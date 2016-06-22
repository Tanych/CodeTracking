class Solution(object):
    def helper(self,k,n,start):
        res=[]
        for i in xrange(start,10):
            # assume the k value are equal, the max is n/k
            if i>n/k:
                return res
            # k==1, only the i equal the n is possible
            if k==1:
                if i==n:
                    return [[i]]
                else:
                    continue
            # depth search every value in the sub depth
            for sub in self.helper(k-1,n-i,i+1):
                res.append([i]+sub)
        return res
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.helper(k,n,1)
        