class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        """
        Dynamic programming
        Definition: DP[i][j] means the min health start from dungeon[i][j]
        to make thing sample, we the heath is 0 after saving the princess
        Also, it needs to start count from [row-1][col-1] to check whether 
        the previous it's possible
        the result should -dp[row-1][col-1]+1
        
        Corner case:
        the last [row-1][col-1]
        dp[row-1][col-1]=0 if dungeon[row-1][col-1]>0 else dungeon[row-1][col-1]
        the col-1 columu(it only can move down)
        if dp[i+1][col-1]+dungeon[i][col-1]>0 
        that means the health could be 0 dp[i][col-1]=0
        if value less than 0, the health should be positive value equal to value
        
        General case
        dp[i][j] has two choice, right or down
        """
        if not dungeon or not dungeon[0]:
            return -1
            
        row=len(dungeon)
        col=len(dungeon[0])
        
        dp=[[0 for _ in xrange(col)] for _ in xrange(row)]
        dp[row-1][col-1]=0 if dungeon[row-1][col-1]>0 else dungeon[row-1][col-1]
        
        # last column
        for i in xrange(row-2,-1,-1):
            tmp=dp[i+1][col-1]+dungeon[i][col-1]
            dp[i][col-1]=tmp if tmp<0 else 0
        
        # last row
        for j in xrange(col-2,-1,-1):
            tmp=dp[row-1][j+1]+dungeon[row-1][j]
            dp[row-1][j]=tmp if tmp<0 else 0
        
        # gernal
        for i in xrange(row-2,-1,-1):
            for j in xrange(col-2,-1,-1):
                # choose the minu heath path if dp[i+1][j=-4 
                # dp[i][j+1]=-5, the better choice is -4, since
                # we need less start health
                tmp=max(dp[i+1][j],dp[i][j+1])+dungeon[i][j]
                dp[i][j]=tmp if tmp<0 else 0
        
        return -dp[0][0]+1
        