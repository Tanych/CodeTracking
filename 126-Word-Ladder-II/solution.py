class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        # build the whole graph for the possible solution
        graph,res={},[]
        bwset,ewset=set([beginWord]),set([endWord])
        path=[beginWord]
        if self.buildGraph(bwset,ewset,graph,True,wordlist):
            self.searchPath(beginWord,endWord,graph,path,res)
        return res
     
    def searchPath(self,beginWord,endWord,graph,path,res):
        if beginWord==endWord:
            res.append(path)
            return
        # search all possible path
        if beginWord in graph:
            for node in graph[beginWord]:
                self.searchPath(node,endWord,graph,path+[node],res)
                
    def addPath(self,graph,word,neighor,isfw):
        # if the path is forward, adding neighor to word
        if isfw:
            graph[word]=graph.get(word,[])+[neighor]
        else:
            graph[neighor]=graph.get(neighor,[])+[word]
            
    def buildGraph(self,bwset,ewset,graph,isfw,wordlist):
        if not bwset:
            return False
            
        if len(bwset)<len(ewset):
            return self.buildGraph(ewset,bwset,graph,not isfw,wordlist)
        
        for w in (bwset|ewset):
            wordlist.discard(w)
            
        find,twset=False,set()
        while bwset:
            word=bwset.pop()
            for i in xrange(len(word)):
                for j in xrange(ord('a'),ord('z')+1):
                    cmbstr=word[:i]+chr(j)+word[i+1:]
                    if cmbstr in ewset:
                        find=True
                        self.addPath(graph,word,cmbstr,isfw)
                    if not find and cmbstr in wordlist:
                        twset.add(cmbstr)
                        self.addPath(graph,word,cmbstr,isfw)
        return find or self.buildGraph(twset,ewset,graph,isfw,wordlist)
        