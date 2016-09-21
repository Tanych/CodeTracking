class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes=[2,3,5]
        plen=len(primes)
        index=[0]*plen
        ugly=[1]+[0]*(n-1)
        
        factors=[i for i in primes]
        for i in xrange(1,n):
            curmin=min(factors)
            ugly[i]=curmin
            for j in xrange(plen):
                if curmin==factors[j]:
                    index[j]+=1
                    factors[j]=ugly[index[j]]*primes[j]
        return ugly[-1]