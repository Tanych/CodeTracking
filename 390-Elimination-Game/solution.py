class Solution(object):
    def ltor(self,n):
        if n<=2: return n
        return 2*self.rtol(n/2)
    
    def rtol(self,n):
        if n<=2: return 1
        # n is odd,it's the same do n/2 from left to right
        if n%2:
            return 2*self.ltor(n/2)
        # n is even,it should be the possible 2*ltor-1
        # suppose 1,2,3,4, when do ltor it could be 4,but we need 3
        else:
            return 2*self.ltor(n/2)-1
            
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ltor(n)