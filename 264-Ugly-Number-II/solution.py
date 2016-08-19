class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes=[2, 3, 5]
        ugly=[0]*n
        
        plen=len(primes)
        index=[0]*plen
        factor=[2,3,5]
        
        ugly[0]=1
        curmin=1
        for i in xrange(1,n):
            curmin=min(factor)
            ugly[i]=curmin
            for j in xrange(plen):
                if curmin==factor[j]:
                    index[j]+=1
                    factor[j]=primes[j]*ugly[index[j]]
        return ugly[-1]
        
        