class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # math: number of n digit: n*9*10^(n-1)
        digitcnt,digitbase=1,9
        # 1. get the candicate digit count,11 locate in 2
        while n>digitcnt*digitbase:
            n-=digitcnt*digitbase
            digitcnt+=1
            digitbase*=10
        # n already minus the g(n-1)
        # n start with the range first number
        rangeidx=(n-1)/digitcnt
        numidx=(n-1)%digitcnt
        num=10**(digitcnt-1)+rangeidx
        return int(str(num)[numidx])
   