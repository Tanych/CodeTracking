class Solution(object):
    def str2int(self,s):
        res=0
        for i in xrange(len(s)):
            res=(res<<3)+(ord(s[i])&7)
        return res
    
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<=10:
            return []
            
        hashmap={}
        res=[]
        for i in xrange(len(s)-9):
            hashmap[self.str2int(s[i:i+10])]=hashmap.get(self.str2int(s[i:i+10]),0)+1
            if hashmap[self.str2int(s[i:i+10])]==2:
                res.append(s[i:i+10])
        return res