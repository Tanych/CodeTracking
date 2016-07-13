class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # the length relate to the solution
        str_len=len(s)
        word_len=len(words[0])
        total_len=word_len*len(words)
        wordset=set(words)
        # using the prehash to match each new one
        prehash=sorted([hash(w) for w in words])
        # building the hash for every possible word
        wordhash=[]
        res=[]
        # building every word possible in hash
        for i in xrange(str_len-word_len+1):
            if s[i:i+word_len] in wordset:
                wordhash.append(hash(s[i:i+word_len]))
            else:
                wordhash.append(None)
                
        # seach whether it's possible to find the same elements
        for i in xrange(str_len-word_len+1):
            # search the number of totoal_len and the corresponding hash
            if wordhash[i] and sorted(wordhash[i:i+total_len:word_len])==prehash:
              res.append(i)
              
        return res
                