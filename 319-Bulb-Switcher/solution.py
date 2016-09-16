class Solution(object):
    def ison(self,k):
        flag=True
        for i in xrange(2,k+1):
            if k%i==0:
                flag=not flag
        return flag
        
    def bruteforce(self,n):
        if n<=0:
            return 0
        res=1
        for i in xrange(4,n+1):
            if self.ison(i):
                res+=1
        return res
        
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.bruteforce(n)
        # find the perfect square from 1-n
        # since the factor of n is double while the 
        # perfect square is not,the have a same factor
        if n==0:
            return 0
        if n==1:
            return 1
        return int(math.sqrt(n))