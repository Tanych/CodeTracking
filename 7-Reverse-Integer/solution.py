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
        sum_int=0  
        while in_x/10:
            sum_int=sum_int*10+ in_x%10
            in_x/=10
        sum_int=sum_int*10+in_x
        
        return negflag*sum_int if sum_int<((1<<31)-1) else 0
        
            