class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=0
        for ch in s:
            newi=t.find(ch,i)
            if newi==-1:return False
            i=newi+1
        return True