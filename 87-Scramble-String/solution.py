class Solution(object):
    def helper(self,s1,s2,mapping):
        n1=len(s1)
        n2=len(s2)
        
        if n1==0 and n2==0:
            return True
        if n1!=n2:
            return False
        if s1==s2:
            return True
        if s1==s2[::-1]:
            return True
        
        # the char should be the same
        count=[0 for _ in xrange(26)]
        
        for i in xrange(n1):
            count[ord(s1[i])-97]+=1
            count[ord(s2[i])-97]-=1
        for i in xrange(26):
            if count[i]:
                return False
        
        if (s1,s2) in mapping:
            return mapping[(s1,s2)]
        
        for i in xrange(1,n1):
            if (self.helper(s1[:i], s2[-i:], mapping) and self.helper(s1[i:], s2[:-i], mapping)) or\
               (self.helper(s1[:i], s2[:i], mapping) and self.helper(s1[i:], s2[i:], mapping)):
                   mapping[(s1,s2)]= True
                   return True
        mapping[(s1,s2)]= False
        return False
            
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        mapping={}
        return self.helper(s1,s2,mapping)
            