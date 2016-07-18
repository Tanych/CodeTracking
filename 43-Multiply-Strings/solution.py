class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
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
                tmval=int(num1_in[j])*int(num2_in[i])+multcarry
                mval=tmval%10
                multcarry=tmval/10
                sum_pos=int(res[i+j])+mval+addcarry
                addcarry=sum_pos/10
                res[i+j]=str(sum_pos%10)
            # deal with the last
            res[i+n1]=str(int(res[i+n1])+addcarry+multcarry)

        rvsres=res[::-1]
        # get rid of the first start 0
        start=0
        while start<len(rvsres) and rvsres[start]=='0':
            start+=1
        
        return ''.join(rvsres[start::])
        