class Solution(object):
    def __init__(self):
        self.path=[]
        
    def dfs(self,t_graph,node):
        arrivals=[]
        
        if node in t_graph:
            arrivals=t_graph[node]
        # pay attention to that at least one valid itinerary
        while arrivals:
            self.dfs(t_graph,arrivals.pop())
        self.path.append(node)
        
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # building the graph of the tickets
        t_graph={}
        for t in tickets:
            if t[0] in t_graph:
                t_graph[t[0]].append(t[1])
                t_graph[t[0]]=sorted(t_graph[t[0]],reverse=True)
            else:
                t_graph[t[0]]=[t[1]]
             
        # recusive
        self.dfs(t_graph,'JFK')
        return self.path[::-1]
        
        # using stack
        """
        path,stck=[],['JFK']
        while stck:
            # iterative get the node from the graph
            while stck[-1] in t_graph and t_graph[stck[-1]]:
                stck.append(t_graph[stck[-1]].pop())
            # stck is the path, now path is the reverse when do pop()
            path.append(stck.pop())
        return path[::-1]
        """ 