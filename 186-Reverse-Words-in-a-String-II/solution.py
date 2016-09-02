class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        idx=0
        for i in xrange(len(s)):
            if s[i]==' ':
                s[idx:i]=reversed(s[idx:i])
                idx=i+1
        # reverse last word
        s[idx:]=reversed(s[idx:])
        s.reverse()