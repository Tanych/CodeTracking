class Solution(object):
    def reduceindex(self,n,primes):
        plen=len(primes)
        if n<=0 or not plen:
            return 0
        # record the index of the factors to use
        indexs=[0]*plen
        factors=[0]*plen
        super_ugly=[1]+[0]*(n-1)
        for i in xrange(plen):
            factors[i]=primes[i]
        
        for i in xrange(1,n):
            curmin=min(factors)
            super_ugly[i]=curmin
            for j in xrange(plen):
                if curmin==factors[j]:
                    # the index record which smaller super ugly number to use
                    indexs[j]+=1
                    # EX,since curmin=2 and the next factor for 2 should be 2*2
                    factors[j]=primes[j]*super_ugly[indexs[j]]
        return super_ugly[-1]
        
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        return self.reduceindex(n,primes)
        super_ugly=[0]*n
        # to record the previous factors used the primes
        # EX. for [2,7,13,19] the index record [2, 0, 0, 0] means
        # next number start from 2 and 7,13,19 should be start from 1
        # super_ugly=[1,  2,   4]
        #             p7        p2
        #             p13
        #             p19
        # everytime ,if the min is the mutilp factor then move on to the next super ugly
        num_prime=len(primes)
        idn_list=[0]*num_prime
        
        super_ugly[0]=1
        
        counter=1
        while counter<n:
            min_list=[]
            for i in xrange(num_prime):
                min_list.append(super_ugly[idn_list[i]]*primes[i])
            min_num=min(min_list)
            
            for i in xrange(num_prime):
                if min_num==super_ugly[idn_list[i]]*primes[i]:
                    idn_list[i]+=1
                    
            super_ugly[counter]=min_num
            counter+=1
        return super_ugly[-1]
        
        
        