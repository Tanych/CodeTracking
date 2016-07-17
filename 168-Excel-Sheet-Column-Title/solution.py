class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res=''
        while n:
            digit=(n-1)%26
            n=(n-1)/26
            res+=chr(digit+ord('A'))
        return res[::-1]