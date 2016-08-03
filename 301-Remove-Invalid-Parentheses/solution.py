class Solution(object):
    def removedfs(self,s,res,last_i,last_j,pair):
        count=0
        # new part
        for i in xrange(last_i,len(s)):
            if s[i]==pair[0]:count+=1
            if s[i]==pair[1]:count-=1
            if count>=0:continue
            for j in xrange(last_j,i+1):
                if s[j]==pair[1] and (s[j-1]!=pair[1] or j==last_j):
                    self.removedfs(s[:j]+s[j+1:],res,i,j,pair)
            return
        
        reverse_str=s[::-1]
        # check the situation leated to (()(()
        # make it reverse and use the same way as ()())()
        if pair[0]=='(':
            self.removedfs(reverse_str,res,0,0,(')','('))
        else:
            # add the final result 
            res.append(reverse_str)
        
        
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # it's a complex problem than what I think
        # EX: ()), ()())(), (()(() 
        # we know how to determine the valid parentheses, using stack or counter
        
        res=[]
        pair=('(',')')
        self.removedfs(s,res,0,0,pair)
        return res
        
        