# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def dfs(self,node,graph):
        if not node:
            return None
        if node.label not in graph:
            newnode=UndirectedGraphNode(node.label)
            graph[node.label]=newnode
            for neigh in node.neighbors:
                self.dfs(neigh,graph)
                graph[node.label].neighbors.append(graph[neigh.label])
                
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        # using the label as the key
        graph={}
        self.dfs(node,graph)
        
        return graph[node.label]
        