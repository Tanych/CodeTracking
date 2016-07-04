class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        # build the whole graph for the possible solution
        graph={}
        path=[beginWord]
        res_paths=[]
        bwset=set([beginWord])
        ewset=set([endWord])
        if self.BFSSearch(bwset,ewset,graph,True,wordlist):
            self.searchPath(beginWord,endWord,graph,path,res_paths)
        return res_paths
     
    def searchPath(self,beginWord,endWord,graph,path,res_paths):
        if beginWord==endWord:
            res_paths.append(path)
            return
        # search all possible path
        if beginWord in graph:
            for node in graph[beginWord]:
                self.searchPath(node,endWord,graph,path+[node],res_paths)
                
    def addPath(self,graph,word,neighor,isfw):
        """
        adding the neighor of words to the graph
        """
        # if the path is forward, adding neighor to word
        if isfw:
            graph[word]=graph.get(word,[])+[neighor]
        # reverse
        else:
            graph[neighor]=graph.get(neighor,[])+[word]
    def BFSSearch(self,bwset,ewset,graph,isfw,wordlist):
        """
        bwset: beginword set
        ewset: endword set
        using BFS search all possible solutions
        if not found return false
        """
        if not len(bwset):
            return False
        # if ewset larger than beset-->reverse to reducing time
        if len(bwset)>len(ewset):
            return self.BFSSearch(ewset,bwset,graph,not isfw,wordlist)
        # remove words already in wordlist
        for word in (bwset|ewset):
            wordlist.discard(word)
        # record all the possible word in next replace
        twset=set()
        # mark whether found
        isFd=False
        while len(bwset):
            word=bwset.pop()
            for ch in xrange(ord('a'),ord('z')+1):
                for i in xrange(len(word)):
                    neighor=word[:i]+chr(ch)+word[i+1:]
                    if neighor in ewset:
                        isFd=True
                        self.addPath(graph,word,neighor,isfw)
                    # conitue find next level
                    if not isFd and neighor in wordlist:
                        twset.add(neighor)
                        self.addPath(graph,word,neighor,isfw)
        # move on or return
        return isFd or self.BFSSearch(twset,ewset,graph,isfw,wordlist)
        