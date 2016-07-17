class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        # if not using the bin search
        if x==1:
            return 1
        
        begin,end=1,x/2
        while begin<end:
            mid=(begin+end)/2
            print mid
            sqt=mid*mid
            if x==sqt:
                return mid
            elif x>sqt:
                begin=mid+1
            else:
                end=mid-1
                
        return begin-1 if x<begin*begin else begin
        """
        r=x
        while r*r>x:
            r=(r+x/r)/2
        return r
        