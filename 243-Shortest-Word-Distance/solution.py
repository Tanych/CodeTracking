class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1=idx2=-1
        minlen=1<<31
        for i in xrange(len(words)):
            if word1==words[i]:
                idx1=i
                if idx2!=-1:
                    minlen=min(minlen,abs(idx2-idx1))
            if word2==words[i]:
                idx2=i
                if idx1!=-1:
                    minlen=min(minlen,abs(idx2-idx1))
        return minlen