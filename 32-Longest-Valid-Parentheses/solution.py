class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n<2:
            return 0
        # to record the valid '()'
        stk=[]
        maxlen=0
        for i in xrange(n):
            if s[i]=='(':
                stk.append(i)
            else:
                # if stk is not empty and top is '(' then math
                if stk and s[stk[-1]]=='(':
                    stk.pop()
                else:
                    stk.append(i)
        # then stk should be the index can't be match
        if not stk:
            return len(s)
        
        # if has no match search the max
        t1,t2=n,0
        while stk:
            t2=stk.pop()
            maxlen=max(maxlen,t1-t2-1)
            t1=t2
        # the first element to deal with
        # since the loop will dump if stk is empty
        # it will not count stk[0]-0
        maxlen=max(maxlen,t1)
        return maxlen
        
            
            