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
        mapping={'A':0,'C':1,'G':2,'T':3}
        
        if len(s)<=10:
            return []
        
        hashmapping={}
        res=[]
        for i in xrange(len(s)-9):
            v=0
            for j in xrange(i,i+10):
               v<<=2
               v|=mapping[s[j]]
               
            hashmapping[v]=hashmapping.get(v,0)+1
            if hashmapping[v]==2:
                res.append(s[i:i+10])
        return res