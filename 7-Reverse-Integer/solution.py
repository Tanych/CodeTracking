class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negflag=1
        in_x=x
        if x<0:
            negflag=-1
            in_x=-x
        if in_x==0:
            return 0
            
        if in_x<10:
            return in_x*negflag
            
        int_res=[]
        while in_x:
            digit=in_x%10
            in_x/=10
            int_res.append(digit)
        #print int_res
        sum_int=0
        start=0
        n=len(int_res)
        # get rid of the zeros
        for i in xrange(len(int_res)):
            if int_res[i]==0:
                start+=1
            else:
                break
            
        res=int_res[start:n]
        for j in xrange(len(res)):
            sum_int+=int(res[j]*math.pow(10,len(res)-j-1))
        # judge the overflow
        return negflag*sum_int if sum_int<((1<<31)-1) else 0
        
            