class Solution(object):
    def helper(self,s,mapping,hashvalue):
        
        if s in hashvalue:
            return hashvalue[s]
            
        if s[0] not in mapping:
            return 0
            
        if len(s)==1 and s[0] in mapping:
            return  1
            
        if len(s)==2:
            if s in mapping and s[0] in mapping and s[1] in mapping:
                return 2
            if s in mapping:
                return 1
                
        left=right=0
        if s and s[0] in mapping:
            left=self.helper(s[1:],mapping,hashvalue)
        if s and s[0:2] in mapping:
            right=self.helper(s[2:],mapping,hashvalue)
        hashvalue[s]=left+right
        return hashvalue[s]
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        mapping={}
        # inital the mapping values
        for i in xrange(26):
            mapping[str(i+1)]=chr(65+i)
        
        hashvalue={}
        return self.helper(s,mapping,hashvalue)
        