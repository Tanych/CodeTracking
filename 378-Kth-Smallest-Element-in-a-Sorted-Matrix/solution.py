class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
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
                count+=t_left
                
            if count<k:
                left=mid+1
            else:
                right=mid
        return left
        