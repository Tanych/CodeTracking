class WallsGate(object):
    def dfs(self, rooms):
        queue = [(i, j, 0) for i, rows in enumerate(rooms) for j, v in enumerate(rows) if not v]

        while queue:
            i, j, step = queue.pop()
            if rooms[i][j] > step:
                rooms[i][j] = step
            for newi, newj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= newi < len(rooms) and 0 <= newj < len(rooms[0]) and step < rooms[newi][newj]:
                    queue.append((newi, newj, step + 1))

    def bfs(self, rooms):
        row=len(rooms)
        col=len(rooms[0])
        queue=[]
        for i in xrange(row):
            for j in xrange(col):
                if rooms[i][j]==0:
                    queue.append(i*col+j)

        while queue:
            x=queue.pop(0)
            i,j=x/col,x%col
            for newi,newj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0 <= newi < len(rooms) and 0 <= newj < len(rooms[0]) and  rooms[newi][newj]==INF:
                    rooms[newi][newj]=rooms[i][j]+1
                    queue.append(newi*col+newj)

    def naivedfs(self, rooms):
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j]==0:
                    self._dfsrev(rooms,i,j)

    def _dfsrev(self,rooms,i,j):
        for newi,newj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0 <= newi < len(rooms) and 0 <= newj < len(rooms[0]) and  rooms[newi][newj]<rooms[i][j]:
                rooms[newi][newj]=rooms[i][j]+1
                self._dfsrev(rooms,newi,newi)
