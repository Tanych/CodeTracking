class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n<=0:
            return []
        matrix=[[0 for _ in xrange(n)] for _ in xrange(n)]
        
        # using four value to record the boundary of the direction
        left=0
        up=0
        down=n-1
        right=n-1
        # 0-move right,1 move down, 2 move left, 3 move up
        direction=0 
        start=1
        while True:
            if direction==0:
                for i in xrange(left,right+1):
                    matrix[up][i]=start
                    start+=1
                up+=1
            if direction==1:
                for i in xrange(up,down+1):
                    matrix[i][right]=start
                    start+=1
                right-=1
            if direction==2:
                for i in xrange(right,left-1,-1):
                    matrix[down][i]=start
                    start+=1
                down-=1
            if direction==3:
                for i in xrange(down,up-1,-1):
                    matrix[i][left]=start
                    start+=1
                left+=1
            
            if up>down or left>right:
                return matrix
            # the next direction
            direction=(direction+1)%4
            