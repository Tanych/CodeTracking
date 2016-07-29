class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stck=[]
        
        for i in xrange(len(tokens)):
            # deal with negative
            if tokens[i].isdigit() or (tokens[i][0]=='-' and tokens[i][1:].isdigit()):
                stck.append(int(tokens[i]))
            elif tokens[i]=='+':
                num1=stck.pop()
                num2=stck.pop()
                stck.append(num2+num1)
            elif tokens[i]=='*':
                num1=stck.pop()
                num2=stck.pop()
                stck.append(num2*num1)
            elif tokens[i]=='-':
                num1=stck.pop()
                num2=stck.pop()
                stck.append(num2-num1)
            elif tokens[i]=='/':
                num1=stck.pop()
                num2=stck.pop()
                # python 2 division problem
                stck.append(num2/num1 if num2*num1>0 else -(abs(num2)/abs(num1)))
        return stck[0] if stck else 0
        