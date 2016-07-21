class Solution(object):
    def checknum(self,s):
        if not s:
            return False
            
        intnum=int(s)
        lens=len(s)
        if intnum>=0 and intnum<=9 and lens>1:
            return False
        if intnum>=10 and intnum<=99 and lens>2:
            return False
        if intnum>=100 and intnum<=255 and lens>3:
            return False
            
        return 0<=intnum<=255
    
        
    def helper(self,s,step,ipstr,res):
        # step means the level to recur
        # only 4 level
        if step==3:
            # if reaches the final level
            if self.checknum(s):
                ipstr+='.'+s
                res.append(ipstr)
                return 
        # else continue to recusive find the result
        for i in xrange(len(s)):
            # try all possible value in 0-255
            if self.checknum(s[:i+1]):
                self.helper(s[i+1:],step+1,ipstr+('.' if ipstr else '')+s[:i+1],res)
        
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<4 or len(s)>12:
            return []
        res=[]
        self.helper(s,0,"",res)
        return res