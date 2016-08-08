class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        """
        it's method to get of node layer by layer from the leaf node
        when you get the single node finally, it's the result
        it's the result
        """
        if n<=1:
            return [0]
        
        #to store each node out degree degree
        outdegree=[0]*n
        
        #get the grap and the corresponding node
        graph={x:[] for x in xrange(n)}
        
        for x,y in edges:
            outdegree[x]+=1
            outdegree[y]+=1
            graph[x].append(y)
            graph[y].append(x)
        
        ret=[]
        queue=[x for x in xrange(n) if outdegree[x]==1]
        
        while queue:
            nextlayer=[]
            ret=queue[:]
            for leaf in queue:
                #for each node correspond to the leaf
                for neighbor in graph[leaf]:
                    #get rid of one layer
                    outdegree[neighbor]-=1
                    if outdegree[neighbor]==1:
                        nextlayer.append(neighbor)
            queue=nextlayer
        return ret
        