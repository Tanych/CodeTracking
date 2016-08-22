class Solution(object):
    def _dfs(self,num,res,n):
        if num>n:
            return 
        res.append(num)
        num=num*10
        if num<=n:
            for i in xrange(10):
                self._dfs(num+i,res,n)
                
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        for i in xrange(1,10):
            self._dfs(i,res,n)
        return res