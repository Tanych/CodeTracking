class Solution(object):
    def gcd(self,a,b):
        if a%b==0:
            return b
        else:
            return self.gcd(b,a%b)
            
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # this math problem need more time to understand prove
        # https://discuss.leetcode.com/topic/49238/math-solution-java-solution
        # deal corner case
        if z==0 or z==x+y:
            return True
        if z>x+y:
            return False
        if x==0:
            return y==z
        if y==0:
            return x==z
        if x==y:
            return z==x

        return z%self.gcd(x,y)==0
        
        
        