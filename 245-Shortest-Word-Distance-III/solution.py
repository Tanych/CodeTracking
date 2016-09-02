class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1=idx2=-1
        minlen=1<<31
        flag=1 if word1==word2 else 0
        times=0
        for i in xrange(len(words)):
            if word1==words[i] and times%2==0:
                idx1=i
                if idx2!=-1:
                    minlen=min(minlen,abs(idx2-idx1))
                times+=flag
            elif word2==words[i]:
                idx2=i
                if idx1!=-1:
                    minlen=min(minlen,abs(idx2-idx1))
                times+=flag
        return minlen