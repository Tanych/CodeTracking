class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        if not n: return 0
        
        # let us do the math
        # f(i)-f(i-1)=sum(arry)-n*arr[n-i]
        sumnum,curfunval=0,0
        
        for i in xrange(n):
            sumnum+=A[i]
            curfunval+=i*A[i]
        maxval=curfunval
        for j in xrange(1,n):
            curfunval+=sumnum-n*A[n-j]
            if curfunval>maxval:
                maxval=curfunval
        return maxval