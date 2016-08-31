class Solution(object):
    def __init__(self):
        self.matching={}
        self.strset=set()
    
    def ismatch(self,pattern,i,strs,j):
        if i==len(pattern) and j==len(strs):
            return True
        if i==len(pattern) or j==len(strs):
            return False
        pchar=pattern[i]
        
        # exist pattern
        if pchar in self.matching:
            matchstr=self.matching[pchar]
            if not strs.startswith(matchstr,j):
                return False
            return self.ismatch(pattern,i+1,strs,j+len(matchstr))
            
        # new pattern
        for k in xrange(j,len(strs)):
            substr=strs[j:k+1]
            if substr in self.strset:
                continue
            
            self.matching[pchar]=substr
            self.strset.add(substr)
            
            if self.ismatch(pattern,i+1,strs,k+1):
                return True
            del self.matching[pchar]
            self.strset.discard(substr)
            
        return False
        
    def wordPatternMatch(self, pattern, strs):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.ismatch(pattern,0,strs,0)
        