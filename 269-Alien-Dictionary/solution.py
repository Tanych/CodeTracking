class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # building a graph through the words order
        graph, degree = {i:[] for i in xrange(26)}, {}
        
        # get unique char and mark unvisited
        for word in words:
            for ch in word:
                if ch not in degree:
                    degree[ord(ch)-97]=0
        # building graph
        for i in xrange(1,len(words)):
            j=0
            preword,curword=words[i-1],words[i]
            while j<min(len(preword),len(curword)):
                if preword[j]!=curword[j]:
                    graph[ord(preword[j])-97]=graph.get(ord(preword[j])-97, []) + [ord(curword[j])-97]
                    degree[ord(curword[j])-97]+=1
                    break
                j+=1
        
        res=''
        queue=[]
        for node in degree:
            if not degree[node]:
                queue.append(node)
                
        while queue:
            peak=queue.pop(0)
            res+=chr(peak+97)
            for node in graph[peak]:
                degree[node]-=1
                if not degree[node]:
                    queue.append(node)
        # has cycle
        for node in degree:
            if degree[node]:
                return ''
        return res
            
        