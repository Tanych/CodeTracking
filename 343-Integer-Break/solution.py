class Solution(object):
    def helper(self,n):
        if n<=4:
            return n
        else:
            return 3*self.helper(n-3)
        
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the max product for 7-10
        # 7--3+4
        # 8--3+3+2
        # 9--3+3+3
        # 10--3+3+4
        # 11--3+3+3+2
        # so it's divide as most as possible 3 and add less than 4
        if n<3:
            return 1
        if n==3:
            return 2
            
        return self.helper(n)