class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #solving in the math way
        #https://en.wikipedia.org/wiki/Trailing_zero
        if n<5:
            return 0
            
        k=int(math.log(n)/math.log(5))
        
        sum=0
        while k>0:
            sum+=int(n/math.pow(5,k))
            k=k-1
        
        return sum