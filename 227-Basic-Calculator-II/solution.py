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
        # the main idea is store the */ result temp
        # and directly add the +- reuls to final result
        # 1(+) -1(-) 2(*) 3(/)
        resnum,num,op=0,0,1
        # to store the temp result product of '/','*'
        product=0
        for i in xrange(len(s)):
            if s[i].isdigit():
                num=num*10+int(s[i])
            elif s[i]=='+' or s[i]=='-':
                # if the previous is '+' or '/'
                # the result of '+' and '/' can be directyly add to the res
                resnum+=product*num if op==2 else self.divideNeg(product,num) if op==3 else op*num
                op=1 if s[i]=='+' else -1
                num=0
            elif s[i]=='*' or s[i]=='/':
                # if previous is '*' or '/', to record the result temp
                # to get the result of all the '*' '/'
                product=product*num if op==2 else self.divideNeg(product,num) if op==3 else op*num
                op=2 if s[i]=='*' else 3
                num=0
        # to deal with the last num and previous result
        resnum+=product*num if op==2 else self.divideNeg(product,num) if op==3 else op*num
        return resnum
        