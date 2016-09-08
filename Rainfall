import heapq

class RainFall(object):
    def smallstep(self, matrix, src, dst):
        n = len(matrix)
        if not n: return -1
        m = len(matrix[0])

        x0, y0, x1, y1 = src[0], src[1], dst[0], dst[1]
        visited = [[False for _ in xrange(m)] for _ in xrange(n)]
        heap, maxheight= [], 0
        heapq.heappush(heap, (matrix[x0][y0], x0 * m + y0))
        while heapq:
            pval, idx = heapq.heappop(heap)
            if pval > maxheight:
                maxheight = pval
            i, j = idx / m, idx % m
            for newi, newj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= newi < m and 0 <= newj < n and not visited[newi][newj]:
                    if (newi, newj) == dst:
                        maxheight = max(maxheight, matrix[x1][y1])
                        return maxheight + 1
                    heapq.heappush(heap, (matrix[newi][newj], newi * m + newj))
                    visited[newi][newj] = True
        return maxheight + 1

t = RainFall()
print t.smallstep([[1, 3, 2, 4], [2, 7, 5, 11], [12, 13, 7, 9], [1, 2, 9, 4]], (0, 0), (3, 3))
