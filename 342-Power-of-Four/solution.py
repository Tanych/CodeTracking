class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        power of 2 n&(n-1)==0
        and even number of 0 in the format
        """
        return num>0 and num&(num-1)==0 and len(bin(num)[2:])%2==1