class Solution(object):
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
            hashmap[s[i:i+10]]=hashmap.get(s[i:i+10],0)+1
        
        for k,v in hashmap.iteritems():
            if v>=2:
                res.append(k)
        return res