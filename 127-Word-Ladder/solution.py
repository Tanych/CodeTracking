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
        while len(bwset)!=0 and len(ewset)!=0:
            # record all the possible transform in wordList 
            tw_trans=set()
            for strs in bwset:
                for i in xrange(len(strs)):
                    # replace with the a-z to check possible solution
                    for k in xrange(ord('a'), ord('z')+1):
                        com_str=strs[:i]+chr(k)+strs[i+1:]
                        # if end, return the min_len
                        if com_str in ewset:
                            return min_len
                        if com_str in wordList:
                            tw_trans.add(com_str)
            #  wordlist delete the same transform with the words
            for li in tw_trans:
                wordList.remove(li)
            if len(tw_trans)<=len(ewset):
                # move on if the possible solution is less then the ending
                bwset=tw_trans
            else:
                # reverse with the small, find one solution in the bigger possible solution
                bwset=ewset
                ewset=tw_trans
            min_len+=1
        # no solution
        return 0
        