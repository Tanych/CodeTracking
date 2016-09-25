class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        row=len(heightMap)
        if not row:
            return 0
        col=len(heightMap[0])
        if not col:
            return 0
        visited=[[False for _ in xrange(col)] for _ in xrange(row)]
        # using heap store the height and pos
        minheap=[]
        # store all the edge case
        for i in xrange(row):
            for j in [0,col-1]:
                visited[i][j]=True
                heapq.heappush(minheap,(heightMap[i][j],i,j))
        for i in [0,row-1]:
            for j in xrange(1,col-1):
                visited[i][j]=True
                heapq.heappush(minheap,(heightMap[i][j],i,j))
        res=0
        while minheap:
            minh,i,j=heapq.heappop(minheap)
            for newi,newj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=newi<row and 0<=newj<col and not visited[newi][newj]:
                    res+=max(0,minh-heightMap[newi][newj])
                    visited[newi][newj]=True
                    heapq.heappush(minheap,(max(minh,heightMap[newi][newj]),newi,newj))
        return res
        
        