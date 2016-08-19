class Solution(object):
    def canFinish(self,numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses<=1:
            return True
        if prerequisites==[]:
            return True
        #get the indegee graph    
        indegree=[0]*numCourses
        g={x:[] for x in xrange(numCourses)}
    
        for x,y in prerequisites:
            indegree[y]+=1
            g[x].append(y)
        
        # adding the start node
        queue=[]
        for i in xrange(numCourses):
            if not indegree[i]:
                queue.append(i)
    
        # no such node, return false
        if not queue:
            return False
    
        # get the out layer level by level
        while queue:
            q=queue.pop(0)
            for j in g[q]:
                indegree[j]-=1
                if indegree[j]==0:
                    queue.append(j)
    
        for i in xrange(numCourses):
            if indegree[i]!=0:
                return False
        return True