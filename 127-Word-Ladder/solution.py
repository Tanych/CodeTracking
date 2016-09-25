class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        bwset=set()
        ewset=set()
        bwset.add(beginWord)
        ewset.add(endWord)
        # start + end
        min_len=2
        while bwset and ewset:
            # record all the possible transform in wordList 
            twset=set()
            # BFS try possible solution from begin to end
            for strs in bwset:
                for i in xrange(len(strs)):
                    # replace with the a-z to check possible solution
                    for k in xrange(ord('a'), ord('z')+1):
                        cmbstr=strs[:i]+chr(k)+strs[i+1:]
                        # if end, return the min_len
                        if cmbstr in ewset:
                            return min_len
                        if cmbstr in wordList:
                            twset.add(cmbstr)
            # wordlist delete the same transform with the words
            # avoid visit the same word mutiple times
            for li in twset:
                wordList.discard(li)
            # speedup--
            # everytime mark down the possible path from begin to end
            # reducing time by checking smallest sizes
            if len(twset)<=len(ewset):
                # move on if the possible solution is less then the ending
                bwset=twset
            else:
                # reverse with the small, find one solution in the bigger possible solution
                bwset=ewset
                ewset=twset
            min_len+=1
        # no solution
        return 0
        