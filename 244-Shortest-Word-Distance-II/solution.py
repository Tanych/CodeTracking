class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.mapping={}
        for i in xrange(len(words)):
            self.mapping[words[i]]=self.mapping.get(words[i],[])+[i]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        wl1=self.mapping[word1]
        wl2=self.mapping[word2]
        i=j=0
        minlen=1<<31
        while i<len(wl1) and j<len(wl2):
            minlen=min(abs(wl1[i]-wl2[j]),minlen)
            if wl1[i]<wl2[j]:
                i+=1
            else:
                j+=1
        return minlen
        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")