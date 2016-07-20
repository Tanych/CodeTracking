class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        resnum=0
        #flag of while it's positive 1,-1
        op=1
        num=0
        stack_ex=[]
        
        for i in xrange(len(s)):
            if s[i].isdigit():
                num=num*10+int(s[i])
                continue
            
            # save the num
            stack_ex.append(op*num)
            
            # change the op value 
            if s[i]=='+':
                op=1
            elif s[i]=='-':
                op=-1
            elif s[i]=='(':
                stack_ex.append('+' if op==1 else '-')
                # need to reset to "+" since "-(1" the first
                # number of '(' should be positive
                op=1
            elif s[i]==')':
                # begin to calc,+,- is the sign to stop add
                # the number inside () is separte by + or -
                parentSum=0
                while stack_ex[-1]!='+' and stack_ex[-1]!='-':
                    parentSum+=stack_ex.pop()
                # if the op before '(' is '-' we need add to neg
                if stack_ex.pop()=='-':
                    parentSum=-parentSum
                # update the sum of num in () to the stack
                stack_ex.append(parentSum)
            # reset the num
            num=0
        
        # deal with the last num
        if num:
            stack_ex.append(op*num)
            
        return sum(stack_ex)
            