class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
            
        if x>(1<<31)-1:
            return False
            
        if x>=0 and x<10:
            return True
        
        if not x%10:
            return False
            
        # only need to reverse half
        sum_int=0
        while x>sum_int:
            sum_int=sum_int*10+x%10
            x/=10
        # odd and even
        return x==sum_int or x==sum_int/10
        