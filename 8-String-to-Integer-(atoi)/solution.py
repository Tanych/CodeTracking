class Solution(object):
    def myAtoi(self, strs):
        """
        :type str: str
        :rtype: int
        """
        n=len(strs)
        if n==0:
            return 0
        
        int_res=[]
        start=0
        neg=1
        for i in xrange(n):
            if strs[i]==" ":
               start+=1
            else:
                break
        # get rid of str
        if len(strs)==start or (strs[start]!='-' and strs[start]!='+' and not strs[start].isdigit()):
            return 0
        
        if strs[start]=='-':
            neg=-1
            start+=1
        elif strs[start]=='+':
            neg=1
            start+=1

        sum_int=0
        while start<len(strs) and strs[start].isdigit():
            digit=ord(strs[start])-ord('1')+1
            sum_int=sum_int*10+digit
            start+=1
            
        if neg==-1 and sum_int>(1<<31):
            return -(1<<31)

        if neg==1 and sum_int>((1<<31)-1):
            return ((1<<31)-1)
        return sum_int*neg
        