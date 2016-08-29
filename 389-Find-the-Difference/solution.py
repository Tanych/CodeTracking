class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        chcnt=[0]*26
        for ch in s:
            chcnt[ord(ch)-97]+=1
        for ch in t:
            chcnt[ord(ch)-97]-=1
        
        for i in xrange(26):
            if chcnt[i]<0:
                return chr(i+97)