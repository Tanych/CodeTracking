class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        # notice that 11 need to count twice
        m=1
        res=0
        while m<=n:
            # divide into two parts
            left=n/m
            right=n%m
            # if the left part end with 0
            # it should the left num divide 10
            # 3124509 -->312450 9 -->31245*10
            if left%10==0:
                res+=left/10*m
            # if ends with 1--> the max on right part is right
            # so it should right+1 on the right part
            elif left%10==1:
                res+=left/10*m+right+1
            # if the left ends larger than 2
            # 31245 09, it should be 3124+1-->2125 
            elif left%10>=2:
                res+=(left/10+1)*m
                
            m*=10
        return res