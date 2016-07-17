class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # COUNT the total
        s=(C-A)*(D-B)+(H-F)*(G-E)
        
        # if not intersection
        if G<=A or E>=C or H<=B or F>=D:
            return s
        # else minius the intersection area
        # using the max and min
        return s-(min(C,G)-max(A,E))*(min(D,H)-max(B,F))
        