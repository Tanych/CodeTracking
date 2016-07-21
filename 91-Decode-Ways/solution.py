class Solution(object):
    def __init__(self):
        self.mapping={}
        # inital the mapping values
        for i in xrange(26):
            self.mapping[str(i+1)]=chr(65+i)
            
        self.hashvalue={}
            
    def helper(self,s):
        
        # save time cost space
        if s in self.hashvalue:
            return self.hashvalue[s]
        
        # if the start not in mapping return 0
        if s[0] not in self.mapping:
            return 0
        
        # if it's the last l
        if len(s)==1 and s[0] in self.mapping:
            return  1
            
        # two elements if two situations
        if len(s)==2 and s in self.mapping:
            return 2 if s[0] in self.mapping and s[1] in self.mapping else 1
                
        left=right=0
        if s and s[0] in self.mapping:
            left=self.helper(s[1:])
        if s and s[0:2] in self.mapping:
            right=self.helper(s[2:])
        # saving the value
        self.hashvalue[s]=left+right
        
        return self.hashvalue[s]
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        return self.helper(s)
        