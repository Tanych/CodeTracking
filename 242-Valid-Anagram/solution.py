class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chars=[0]*26
        
        for i in xrange(len(s)):
            chars[ord(s[i])-97]+=1
        
        for i in xrange(len(t)):
            chars[ord(t[i])-97]-=1
        
        for nums in chars:
            if nums!=0:
                return False
        return True