class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # n number, if n starts with 1, there are (n-1)! number
        # to find which number in, k/fac+1
        
        fac,res=1,''
        for i in xrange(1,n):
            fac*=i
        k-=1
        num=['1','2','3','4','5','6','7','8','9']
        for i in xrange(n-1,-1,-1):
            cur=num[k/fac]
            res+=str(cur)
            num.remove(cur)
            if i!=0:
                k%=fac
                fac/=i
        return res
        
                