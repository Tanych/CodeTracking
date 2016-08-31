class Solution(object):
    def __init__(self):
        self.memo={}
        
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        return self.isNextCanWin(s)
        
    def isNextCanWin(self,s):
        if s in self.memo:
            return self.memo[s]
        
        for i in xrange(len(s)-1):
            if s[i:i+2]=='++' and not self.isNextCanWin(s[0:i]+'--'+s[i+2:]):
                self.memo[s]=True
                return True
        self.memo[s]=False
        return False
            
    