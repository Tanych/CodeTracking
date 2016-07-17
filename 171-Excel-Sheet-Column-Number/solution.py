class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        sum=0
        for i in xrange(n):
            sum+=int((ord(s[i])-ord('A')+1)*math.pow(26,n-i-1))
        
        return sum