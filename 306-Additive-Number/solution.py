class Solution(object):
    def isvalid(self,num1,num2,strs):
        res_sum=str(int(num1)+int(num2))
        res_len=len(res_sum)
        
        if len(strs)<res_len:
            return False
        if strs==res_sum:
            return True
        if res_sum==strs[:res_len]:
            # check the left part
            return self.isvalid(num2,res_sum,strs[res_len:])
        # not equal return false
        return False
        
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # using the recusing way to do solve the problem
        num1=''
        num2=''
        n=len(num)
        # do not need to access all, only the n/3 part
        # since the num1+num2=num3 with max n/3 length
        for i in xrange(n/3):
            num1=num[:i+1]
            # get rid of the 01,02
            if num1[0]=='0' and len(num1)>1:
                continue
            for j in xrange(i+1,n):
                num2=num[i+1:j+1]
                if num2[0]=='0' and len(num2)>1:
                    continue
                if self.isvalid(num1,num2,num[j+1:]):
                    return True
        return False
                