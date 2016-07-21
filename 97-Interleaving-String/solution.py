class Solution(object):
    def helper(self,s1,s2,s3,hasvisited):
        if (s1,s2,s3) in hasvisited:
            return hasvisited[(s1,s2,s3)]
            
        if not s1 and not s2 and not s3:
            return True
        
        if not s1:
            return s2==s3
        if not s2:
            return s1==s3
        # using the hashmap to record the same(s1,s2,s3) to reduce same count
        # EX: if start with s1, the s1 becomes to reduce len1, s2 reduce to len2
        # if these not exist, then rollback to recount start s2, s2 reduct to len2
        # s1 reduce to s1, this time it's no need to count the again
        s2res=s1res=False
        if s2[0]==s3[0]:
            s2res= self.helper(s1,s2[1:],s3[1:],hasvisited)
        if s1[0]==s3[0]:
            s1res= self.helper(s1[1:],s2,s3[1:],hasvisited)
        
        hasvisited[(s1,s2,s3)]=s1res|s2res
        return hasvisited[(s1,s2,s3)]
        
                
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        hasvisited={}
        return self.helper(s1,s2,s3,hasvisited)
        