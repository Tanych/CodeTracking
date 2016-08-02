class Solution(object):
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
                
        route,stck=[],['JFK']
        while stck:
            # iterative get the node from the graph
            while stck[-1] in t_graph and t_graph[stck[-1]]:
                stck.append(t_graph[stck[-1]].pop())
            # stck is the route, now route is the reverse when do pop()
            route.append(stck.pop())
        return route[::-1]
            