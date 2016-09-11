class Solution(object):
    def dfsquery(self,graph,vals,start,end,visited):
        if start==end and start in graph:
            return 1.0
        if (start,end) in vals:
            return vals[(start,end)]
        # dfs query
        if start in graph:
            for subnode in graph[start]:
                if subnode in visited:
                    continue
                visited.add(subnode)
                ressub=self.dfsquery(graph,vals,subnode,end,visited)
                if ressub!=-1.0:
                    return vals[(start,subnode)]*ressub
                else:
                    visited.discard(subnode)
                    return -1.0
        return -1.0
        
        
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type query: List[List[str]]
        :rtype: List[float]
        """
        vals,graph={},{}
        n=len(equations)
        
        # building directed graph
        for i in xrange(n):
            a,b=equations[i][0],equations[i][1]
            graph[a]=graph.get(a,[])+[b]
            graph[b]=graph.get(b,[])+[a]
            vals[(a,b)]=values[i]
            vals[(b,a)]=1.0/values[i]
            
        qlen=len(queries)
        res=[0.0]*(qlen)
        for i in xrange(qlen):
            # check a-->b has the path
            res1=self.dfsquery(graph,vals,queries[i][0],queries[i][1],{queries[i][0]})
            if res1==-1.0:
                # if not check path b--->a
                res[i]=1.0/self.dfsquery(graph,vals,queries[i][1],queries[i][0],{queries[i][1]})
            else:
                res[i]=res1
        return res