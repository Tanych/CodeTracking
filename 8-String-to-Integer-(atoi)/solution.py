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
        nwstrs=strs[start:n]
        if len(nwstrs)==0 or (nwstrs[0]!='-' and nwstrs[0]!='+' and not nwstrs[0].isdigit()):
            return 0
        
        if nwstrs[0]=='-':
            neg=-1
            nwstrs=nwstrs[1:]
        elif nwstrs[0]=='+':
            neg=1
            nwstrs=nwstrs[1:]
            
        for i in xrange(len(nwstrs)):
            if nwstrs[i].isdigit():
                int_res.append(ord(nwstrs[i])-ord('1')+1)
            else:
                break
        #print int_res
        sum_int=0
        for j in xrange(len(int_res)):
            sum_int+=int(int_res[j]*math.pow(10,len(int_res)-j-1))
            
        if neg==-1 and sum_int>(1<<31):
            return -(1<<31)

        if neg==1 and sum_int>((1<<31)-1):
            return ((1<<31)-1)
        return sum_int*neg
        