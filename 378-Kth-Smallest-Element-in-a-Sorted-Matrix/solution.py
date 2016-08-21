class Solution(object):
    def minheap(self,matrix,k):
        """
        the same idea for get the kth element from n list
        """
        row=len(matrix)
        if row<=0:return -1
        col=len(matrix[0])
        heap=[]
        for j in xrange(col):
            heapq.heappush(heap,(matrix[0][j],0,j))
        for i in xrange(k-1):
            peak,ridx,cidx=heapq.heappop(heap)
            if ridx<row-1:
               heapq.heappush(heap,(matrix[ridx+1][cidx],ridx+1,cidx))
        return heapq.heappop(heap)[0]
        
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        """
        The time complexity is O(n * log(n) * log(N)), 
        N is the search space ranging from the smallest num to the biggest num
        log(N) can't assume as constant so it's would be o(n*log(n))
        
        if we use quickselect it would be o(number of element) it's would be O(n^2)
        """
        return self.minheap(matrix,k)
        
        n=len(matrix)
        left,right=matrix[0][0],matrix[n-1][n-1]
        
        while left<right:
            mid=left+(right-left)/2
            # count number less than mid
            count=0
            # search every row
            for i in xrange(n):
                row=matrix[i]
                # search the upper bound
                t_left,t_right=0,n
                while t_left<t_right:
                    t_mid=(t_left+t_right)/2
                    if row[t_mid]>mid:
                        t_right=t_mid
                    else:
                        t_left=t_mid+1
                # mark the count
                count+=t_left
                
            if count<k:
                left=mid+1
            else:
                right=mid
        return left
        