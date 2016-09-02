class Solution(object):
    def isreplace(self,s,t):
        replace=False
        for i in xrange(len(s)):
            if s[i]!=t[i]:
                if replace: 
                    return False
                replace=True
        return replace
    
    def isdelete(self,s,t):
        for i in xrange(len(t)):
            if s[i]!=t[i]:
                return s[i+1:]==t[i:]
        return True
    
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen,tlen=len(s),len(t)
        if slen==tlen: return self.isreplace(s,t)
        if slen-tlen==1: return self.isdelete(s,t)
        if tlen-slen==1: return self.isdelete(t,s)
        return False
        
        
        
        