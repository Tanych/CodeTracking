class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 10
        if n==0:
            return 1
        # the base
        num_base=9
        # the first get rid of 0
        res=9
        times=n
        while times>1:
            res*=num_base
            num_base-=1
            times-=1
        return res+self.countNumbersWithUniqueDigits(n-1)