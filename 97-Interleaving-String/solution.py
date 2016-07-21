class Solution(object):
    def isInterleaveDP(self,s1, s2, s3):
        """
        O(m*n) space 
        """
        len1,len2,len3=len(s1),len(s2),len(s3)
        if len1+len2!=len3:
            return False
        # define: dp[i][j] means the s1(0,i) and s2(0,j) interveal in s3(0,i+j)
        dp=[[True for _ in xrange(len2+1)] for _ in xrange(len1+1)]
        
        # initial value, only check s1, s3,suppose s2 is empty
        for i in xrange(1,len1+1):
            dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]
        # only check s2 s3,suppose s1 is empty
        for j in xrange(1,len2+1):
            dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]
        for i in xrange(1,len1+1):
            for j in xrange(1,len2+1):
                dp[i][j]=(dp[i-1][j] and s1[i-1]==s3[i-1+j]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[-1][-1]
        
    def isInterleaveDP2(self,s1, s2, s3):
        """
        O(n) space 
        """
        len1,len2,len3=len(s1),len(s2),len(s3)
        if len1+len2!=len3:
            return False
        # define: dp[i][j] means the s1(0,i) and s2(0,j) interveal in s3(0,i+j)
        dp=[True for _ in xrange(len2+1)]
        
        # initial set up the table of 
        for j in xrange(1,len2+1):
            dp[j]=dp[j-1] and (s2[j-1]==s3[j-1])
        
        # we can image it only can move right and down in the matrix
        for i in xrange(1,len1+1):
            # inital the row value, since we only need the value in the previous column
            dp[0]=dp[0] and s1[i-1]==s3[i-1]
            for j in xrange(1,len2+1):
                # the dp[j] in left = is the new row cossrespond to [i][j]
                # the dp[j] in right = is the previous row value, [i-1][j-1]
                # dp[j-1] is the previous result 
                dp[j]=(dp[j] and s1[i-1]==s3[i-1+j]) or (dp[j-1] and s2[j-1]==s3[i+j-1])
                
        return dp[-1]
        
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
        """
        <Longest Test case>
        "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb",
        "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc",
        "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"
        """
        """
        # 1.recusive
        hasvisited={}
        return self.helper(s1,s2,s3,hasvisited)
        """
        # 2.dp with O(m*n)
        #return self.isInterleaveDP(s1,s2,s3)
        # 3.dp with O(n)
        return self.isInterleaveDP2(s1,s2,s3)
        