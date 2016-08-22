class Solution(object):
    def _dfs(self,num,res,n):
        if num>n:
            return 
        res.append(num)
        num=num*10
        if num<=n:
            for i in xrange(10):
                self._dfs(num+i,res,n)
    def sovleOn(self,n):
        res=[]
        cur=1
        for i in xrange(1,n+1):
            res.append(cur)
            if cur*10<=n:
                cur=cur*10
            # if the num not end with 9,plus 1
            # since if 19 the next should 2 not 20
            elif cur%10!=9 and cur+1<=n:
                cur+=1
            else:
                # get the 199--2 499--5
                while (cur/10)%10==9:
                    cur/=10
                cur=cur/10+1
        return res
                
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return self.sovleOn(n)
        res=[]
        for i in xrange(1,10):
            self._dfs(i,res,n)
        return res