class Solution(object):
    def smallkpow(self,a,k):
        """
        k>=0 and k<=10
        """
        #a%=1337
        res=1
        for i in xrange(k):
            res=(res*a)%1337
        return res
            
        
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # it's relative easy to get te pow if k<=10
        # a^123456=(a^12345)^10*a^6
        if not b:
            return 1
        last=b.pop()
        return self.smallkpow(self.superPow(a,b),10)*self.smallkpow(a,last)%1337
        