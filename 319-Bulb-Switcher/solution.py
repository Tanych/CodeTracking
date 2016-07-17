class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        rounds=2
        
        res=[1]*n
        
        while rounds<=n:
            for i in xrange(rounds-1,n):
                if (i+1)%rounds==0:
                    res[i]^=1
            rounds+=1
        #print res
        cnt=0
        for i in xrange(n):
            if res[i]==1:
                cnt+=1
        return cnt