class Solution(object):
    def _findsub(self,left,right,slen,wlen,t_wlen,cntword,res,s):
        curr={}
        while right+wlen<=slen:
            word=s[right:right+wlen]
            right+=wlen
            
            if word not in cntword:
                # start new pos
                left=right
                curr.clear()
            else:
                # cnt currurent word
                curr[word]=curr.get(word,0)+1
                # if current has more mutilp words, get rid of the left part
                while curr[word]>cntword[word]:
                    # the left word should get out
                    curr[s[left:left+wlen]]-=1
                    # move left
                    left+=wlen
                # if the length equal the total tagert
                if right-left==t_wlen:
                    res.append(left)
            
    def findsubstring_dict(self, s,words):
        str_len=len(s)
        word_len=len(words[0])
        total_wlen=word_len*len(words)
        
        # building dict for the words
        cntword={}
        for word in words:
            cntword[word]=cntword.get(word,0)+1
        
        res=[]
        for i in xrange(min(word_len,str_len-total_wlen+1)):
            self._findsub(i,i,str_len,word_len,total_wlen,cntword,res,s)
        return res
        
        
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        return self.findsubstring_dict(s,words)
        
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
                