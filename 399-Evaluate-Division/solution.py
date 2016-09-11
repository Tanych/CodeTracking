class Solution(object):
    def qurey(self,graph,mapping,start,end,visited):
        if start==end and start in graph:
            return 1.0
            
        if (start,end) in mapping:
            return mapping[(start,end)]
        
        if start in graph:
            for subnode in graph[start]:
                if subnode not in visited:
                    visited.add(subnode)
                    ressub=self.qurey(graph,mapping,subnode,end,visited)
                    if ressub!=-1.0:
                        return mapping[(start,subnode)]*ressub
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
        mapping={}
        graph={}
        
        n=len(equations)
        for i in xrange(n):
            graph[equations[i][0]]=graph.get(equations[i][0],[])+[equations[i][1]]
            graph[equations[i][1]]=graph.get(equations[i][1],[])+[equations[i][0]]
            mapping[(equations[i][0],equations[i][1])]=values[i]
            mapping[(equations[i][1],equations[i][0])]=1.0/values[i]
        #print graph ,mapping
        
        qlen=len(queries)
        res=[0.0]*(qlen)
        for i in xrange(qlen):
            res1=self.qurey(graph,mapping,queries[i][0],queries[i][1],{queries[i][0]})
            if res1==-1.0:
                res[i]=1.0/self.qurey(graph,mapping,queries[i][1],queries[i][0],{queries[i][1]})
            else:
                res[i]=res1
        
        return res