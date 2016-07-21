class Solution(object):
    def helper(self,s1,s2,s3):
        if not s1 and not s2 and not s3:
            return True
        
        if not s1:
            return s2==s3
        if not s2:
            return s1==s3
            
        if s1[0]==s3[0] and s2[0]==s3[0]:
            return self.helper(s1[1:],s2,s3[1:])|self.helper(s1,s2[1:],s3[1:])
        elif s2[0]==s3[0]:
            return self.helper(s1,s2[1:],s3[1:])
        elif s1[0]==s3[0]:
            return self.helper(s1[1:],s2,s3[1:])
    
        return False
        
                
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return self.helper(s1,s2,s3)
        