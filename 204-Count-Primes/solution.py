class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        A naive way to solve the problem is to judge every number from 
        the range[m,n] isprime, isprime can be optimal take n^(1/2)
        so the total is n^(1.5).
        
        The better way is using space to mark the possible solution
        """
        isprime=[True]*n
        i=2
        while i*i<n:
            if not isprime[i]:
                i+=1
                continue
            j=i*i
            while j<n:
                isprime[j]=False
                j+=i
            i+=1

        cnt=0 
        for k in xrange(2,n):
            if isprime[k]: cnt+=1
        return cnt
            