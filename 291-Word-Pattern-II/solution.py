class Solution(object):
    def __init__(self):
        self.matching={}
        # avoid a,b use the same key
        self.strset=set()
    
    def ismatch(self,pattern,i,strs,j):
        if i==len(pattern) and j==len(strs):
            return True
        if i==len(pattern) or j==len(strs):
            return False
        p=pattern[i]
        if p in self.matching:
            if not strs.startswith(self.matching[p],j):
                return False
            return self.ismatch(pattern,i+1,strs,j+len(self.matching[p]))
        # new pattern
        for k in xrange(j,len(strs)):
            substr=strs[j:k+1]
            # avoid a,b use same key
            if substr in self.strset:
                continue
            self.matching[p]=substr
            self.strset.add(substr)
            if self.ismatch(pattern,i+1,strs,k+1):
                return True
            del self.matching[p]
            self.strset.discard(substr)
        return False
        
    def wordPatternMatch(self, pattern, strs):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.ismatch(pattern,0,strs,0)
        