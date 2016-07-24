class Solution(object):
    def divideNeg(self,a,b):
        """
        python divide -3/2==-2  
        """
        if a*b<0:
            return -(abs(a)/abs(b))
        else:
            return a/b
            
    def calcWithMD(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # using stack to store the result
        numstk=[]
        num=0
        # 1(+),-1(-),2(*),3(/)
        # should start with positive num
        op='+'
        
        for i in xrange(len(s)):
            if s[i].isdigit():
                num=num*10+int(s[i])
            if (not s[i].isdigit() and s[i]!=' ') or i==len(s)-1:
                # the op is the previous op
                # 14*3/2 whien s[i]=='*' ,op is the first '+'
                if op=='+' or op=='-':
                    numstk.append(num if op=='+' else -num)
                elif op=='*' or op=='/':
                    # get the previous op
                    opval=numstk.pop()
                    # push the result
                    numstk.append(opval*num if op=='*' else self.divideNeg(opval,num))
                # update op
                op=s[i]
                num=0
        return sum(numstk) if numstk else 0

    def calculate(self, s):
        n=len(s)
        if not s:
            return -1

        stck=[]
        i=0
        while i<n:
            if s[i]==')':
                strop=''
                while stck and stck[-1]!='(':
                    strop+=stck.pop()
                value=self.calcWithMD(strop[::-1])
                if stck and stck[-1]=='(':
                    stck.pop()
                # deal with mutil --
                if stck and stck[-1]=='-':
                    if value<0:
                        stck.pop()
                        stck.append('+')
                        value=-value
                # insert the reverse value since, pop
                # will get the reverse string
                stck.append(str(value)[::-1])
            else:
                stck.append(s[i])
            i+=1
            
        # calulate the last op without ()
        strop=''
        while stck:
            strop+=stck.pop()
        value=self.calcWithMD(strop[::-1])
        return value
            