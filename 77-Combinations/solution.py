class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(start,reslevel,step):
            if step==k:
                res.append(reslevel)
                return
            # if the left number of elements less then the needed
            # stop!!!..make the calc faster
            if n-start+1<k-len(reslevel):
                return
            #search
            for i in xrange(start,n+1):
                dfs(i+1,reslevel+[i],step+1)
                
        res=[]
        dfs(1,[],0)
        return res
        
        
        