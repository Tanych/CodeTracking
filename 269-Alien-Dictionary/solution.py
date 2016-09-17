class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph={chr(i+97):[] for i in xrange(26)}
        degree={}
        
        # get the degree char
        for word in words:
            for ch in word:
                if ch not in degree:
                    degree[ch]=0
        #build graph
        n=len(words)
        for i in xrange(1,n):
            j=0
            preword,curword=words[i-1],words[i]
            while j<min(len(preword),len(curword)):
                if preword[j]!=curword[j]:
                    graph[preword[j]].append(curword[j])
                    degree[curword[j]]+=1
                    break
                j+=1
        print graph
        queue=collections.deque([])
        for node in degree:
            if not degree[node]:
                queue.append(node)
        
        res=[]
        while queue:
            peak=queue.popleft()
            res.append(peak)
            for node in graph[peak]:
                degree[node]-=1
                if not degree[node]:
                    queue.append(node)
        # check valid
        for node in degree:
            if degree[node]:
                return ""
        return ''.join(res)
                
            
        