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
        # https://discuss.leetcode.com/topic/49257/share-my-0ms-c-solution-with-proof-and-explanation/2
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
        x_cal=x if y>x else y
        y_cal=y if y>x else x
        
        r=y_cal%x_cal
        # 3,6
        # if x,y is mutilp,z should also be mutilp
        if r==0:
            return z%x_cal==0
        else:
            print z,r,self.gcd(r,x_cal)
            return z%self.gcd(r,x_cal)==0
        
        
        