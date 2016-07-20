class Solution(object):
    def divideNeg(self,a,b):
        """
        python divide -3/2==-2  
        """
        if a*b<0:
            return -(abs(a)/abs(b))
        else:
            return a/b
            
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # using stack to store the result
        numstk=[]
        resnum=0
        num=0
        # 1(+),-1(-),2(*),3(/)
        # should start with positive num
        op=1
        # inital the product with 1
        product=1
        
        for i in xrange(len(s)):
            if s[i].isdigit():
                num=num*10+int(s[i])
            if s[i]=='+' or s[i]=='-':
                numstk.append(product*num if op==2 else self.divideNeg(product,num) if op==3 else op*num)
                op=1 if s[i]=='+' else -1
                num=0
            elif s[i]=='*' or s[i]=='/':
                product=product*num if op==2 else self.divideNeg(product,num) if op==3 else op*num
                op=2 if s[i]=='*' else 3
                num=0
        numstk.append(product*num if op==2 else self.divideNeg(product,num) if op==3 else op*num)
        return sum(numstk)
        