class Solution(object):
    def removedfs(self,s,res,last_i,last_j,pair):
        """
        last_i: the position occurs non-balance (), mean ) is more than (
        for the pair'()'.
        last_j: the last delete position of pair ), if we don't record the 
        position we might get duplicate results.
        pair: for the op oder or reverse order.
        """
        count=0
        # new part
        for i in xrange(last_i,len(s)):
            if s[i]==pair[0]:count+=1
            if s[i]==pair[1]:count-=1
            if count>=0:continue
            for j in xrange(last_j,i+1):
                # j==last_j focus on ))) or (( this situation
                if s[j]==pair[1] and (j==last_j or s[j-1]!=pair[1]):
                    print s,last_j,j,s[j-1],pair[1]
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
        
    def bruteforce(self,s):
        def isvalid(s):
            count=0
            for ch in s:
                if ch=='(':
                    count+=1
                elif ch==')':
                    count-=1
                    if count<0:
                        return False
            return count==0
        level={s}
        while True:
            valid=filter(isvalid, level)
            if valid:
                return valid
            level={s[:i]+s[i+1:] for s in level for i in xrange(len(s))}
            
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # it's a complex problem than what I think
        # EX: ()), ()())(), (()(() 
        # we know how to determine the valid parentheses, using stack or counter
        #return self.bruteforce(s)
        res=[]
        pair=('(',')')
        self.removedfs(s,res,0,0,pair)
        return res
        
        