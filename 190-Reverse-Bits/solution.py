class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=31
        sum_num=0
        while i>=0:
            if n&1:
                sum_num+=(1<<i)
            n=n>>1
            i-=1
            
        return sum_num