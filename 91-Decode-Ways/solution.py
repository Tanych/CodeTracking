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
    
    def numDecodingsDP(self,s):
        """
        definition: dp[i], how many way to decode the first i ele
        initial:dp[1]=1 if s[0]!='0' else 0
        State transfer:
        s[i]!=0 dp[i+1]=dp[i] else dp[i]=0
        suppose 2110 --
        if s[i-1,i+1] belongs to (10,26) dp[i+1]=dp[i+1]+dp[i-1]
        """
        n=len(s)
        dp=[0 for _ in xrange(n+1)]
        dp[0]=1
        dp[1]=1 if s[0]!='0' else 0
        
        for i in xrange(2,n+1):
            if s[i-1]!=0:
                dp[i]=dp[i-1]
            dbdigit=int(s[i-2:i])
            # it should two situtation that makes contribution to 
            # dp[i-1] means get rid of the 2 number 1123-->(11)+(1123)
            if 10<=dbdigit<=26:
                dp[i]+=dp[i-2]
                
        return dp[-1]
    
    def numDecodingsDP2(self,s):
        n=len(s)
        if s[0]=='0':
            return 0
        
        #for i in xrange(1,n):
        #    if s[i]=='0' and s[i-1]!='1' and s[i-1]!='2':
        #        return 0
        #using three value to record the previous dp values
        #dp[0]
        dp_prepre=1
        #dp[1]
        dp_pre=1
        #dp[1:] change the value
        # if only one value, it should be 1
        dp_cur=1
        
        for i in xrange(1,n):
            dp_cur=0
            if s[i]!="0":
                # same as the previous
                dp_cur+=dp_pre
            if s[i-1]=='1' or (s[i-1]=='2' and s[i]<='6'):
                dp_cur+=dp_prepre
                
            # move on the three pointers
            dp_prepre=dp_pre
            dp_pre=dp_cur
            
        return dp_cur
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        return self.numDecodingsDP2(s)
        