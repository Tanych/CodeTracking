class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # not using int or str to convert
        
        if num1=='0' or num2=='0':
            return '0'

        n1=len(num1)
        n2=len(num2)
        num1_in=num1[::-1]
        num2_in=num2[::-1]

        res=['0' for _ in xrange(n1+n2)]

        # every num in num2
        for i in xrange(n2):
            #add carry for the different pos add
            addcarry=0
            # the carry record the number multiply
            multcarry=0
            for j in xrange(n1):
                tmval=(ord(num1_in[j])-48)*(ord(num2_in[i])-48)+multcarry
                mval=tmval%10
                multcarry=tmval/10
                sum_pos=(ord(res[i+j])-48)+mval+addcarry
                addcarry=sum_pos/10
                res[i+j]=chr(sum_pos%10+48)
                
            # deal with the last carry
            # the first carry comes from the addcarry means add all the value in the same i+j
            # the second carry come from the mutilp op 323*24-->3*4--12-->multcarry 1
            res[i+n1]=chr(ord(res[i+n1])+addcarry+multcarry)

        rvsres=res[::-1]
        # get rid of the first start 0
        start=0
        while start<len(rvsres) and rvsres[start]=='0':
            start+=1
        
        return ''.join(rvsres[start::])
        