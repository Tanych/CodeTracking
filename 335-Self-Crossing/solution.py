class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        n=len(x)
        if n<4:
            return False
        # start with the fourth element
        i=3
        
        while i<n:
            # if i cross with i-3, it's very simple
            if x[i]>=x[i-2] and x[i-1]<=x[i-3]:
                return True
            # if i cross with i-4, it build a cross with 5 steps
            # s1 [2,4,4,4,2]
            #(2)****(1)
            #   *  *(0) 
            #   *  *(5)
            #(3)****(4)
            # the last step should be larger than the diff between i-2 and i-4
            if i>=4 and x[i-1]==x[i-3] and x[i-2]-x[i-4]<=x[i]:
                return True
            
            # i cross with i-5 
            # [3,6,5,9,4,6]
            #(2)******(1)
            #   * *******(6)
            #   * (7)*  * 
            #   *   (0) *
            #(3)*********(4)
            # the (4-6) should betwen (0-1)
            # the (6-7) should larger than (4-3) minus (2-1)
            if i>=5 and x[i-1]<=x[i-3] and x[i-1]>=x[i-3]-x[i-5] and x[i-2]>=x[i-4] and x[i]>=x[i-2]-x[i-4]:
                return True
            i+=1
        return False