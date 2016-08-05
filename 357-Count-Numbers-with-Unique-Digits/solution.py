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
        dp,i=1,1
        while i<=n and i<10:
            dp+=num_base
            num_base*=(10-i)
            i+=1
        return dp