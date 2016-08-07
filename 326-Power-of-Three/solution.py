class Solution(object):
    def __init__(self):
        self.maxpower=self.max3power_32b()
        
    def max3power_32b(self):
    	i,n=0,3
    	while n<(1<<31-1):
    		n=3**i
    		i+=1
    	return n

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and self.maxpower%n==0
        