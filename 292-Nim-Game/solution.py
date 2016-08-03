class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        n==1,2,3 true
        n=4, false
        n=5, 1+4 True
        n=6, 2+4 True
        n=7, 3+4 True
        n=8, 1+7,2+6,3+5, all  False
        """
        return not n%4==0
        