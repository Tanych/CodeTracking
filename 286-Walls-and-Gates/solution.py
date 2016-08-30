class Solution(object):
    def dfs(self,rooms):
        # get all gate position
        queue=[(i,j,0) for i,rows in enumerate(rooms) for j,v in enumerate(rows) if not v]
        while queue:
            i,j,depth=queue.pop()
            # has a min path to gate and update
            if depth<rooms[i][j]:
                rooms[i][j]=depth
            for newi,newj in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=newi<len(rooms) and 0<=newj<len(rooms[0]) and depth<rooms[newi][newj]:
                    queue.append((newi,newj,depth+1))
    def bfs(self,rooms):
         # get all gate position
        queue=[(i,j) for i,rows in enumerate(rooms) for j,v in enumerate(rows) if not v]
        while queue:
            # pop the fist insert
            i,j=queue.pop(0)
            for newi,newj in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=newi<len(rooms) and 0<=newj<len(rooms[0]) and rooms[newi][newj]==2147483647:
                    rooms[newi][newj]=rooms[i][j]+1
                    queue.append((newi,newj))
                    
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        self.bfs(rooms)
        