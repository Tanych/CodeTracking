class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        res=0
        tlen=0
        for i in xrange(len(s)):
            if s[i]==' ':
                tlen=0
            else:
                tlen+=1
                # using res to record the last valid length
                # "adsf    " is 4 not 0
                res=tlen
        return res