class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
        I think if not in-place, the question should be very simple
        However, the interview might follow up to keep replace in-place
        That's the total target.
        """
        n=len(s)
        if n<=numRows:
            return s
        
        if not s or not numRows:
            return ''
        
        # the first row index transfer offset
        # numRows-2 means get rid of the first and last row since they don't store
        # there are 2 colum between the element in first row
        # the last 2 is the element in first row and last row
        idxfirst=(numRows-2)*2+2
        
        # the number of elements between the first rows
        # 3 means the element is the first row and last row
        btnum=numRows*2-3
        
        res=''
        # deal with the first row
        i=0
        while i<n:
            res+=s[i]
            i+=idxfirst
        
        # deal with the item bewteen each gaps
        """
        Refs: https://discuss.leetcode.com/topic/50181/4ms-c-solution-with-explanation
        0 1 2 3 4 5 6 7 8 9 10 11 12 13    < Old Offsets
        P A Y P A L I S H I R  I  N  G
        0       1       2         3        < Boundary Offsets
        t1 <->  t2                         < Scan Window 0 - 4
                t1 <->  t2                 < Scan Window 4 - 8
                        t1  <->   t2       < Scan Window 8 - 12
                                  t1       < Scan Window 12 -13
        """
        k=0
        c=1
        while k<btnum:
            t1=0
            t2=idxfirst
            while t1<n or t2<n:
                # the element t1+1(1 is the relative offeset) and t2-1 should be the next element
                # t1 t2 like a two pointer, run with two diffirent direction and meet with other 
                if t1+offset<n:
                    res+=s[t1+offset]
                # if t1 and t2 reach the same pos
                if t1+offset!=t2-offset and t2-offset<n:
                    res+=s[t2-offset]
                    
                # move to next windows
                t1=t2
                t2=t2+idxfirst
            c+=1
            k+=2
        return res
        