class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s:
            return []
        wlen,num,n=len(words[0]),len(words),len(s)
        
        cntword,res={},[]
        # build target words count
        for word in words:
            cntword[word]=cntword.get(word,0)+1
            
        for i in xrange(n-num*wlen+1):
            seen={}
            j=0
            while j<num:
                subword=s[i+j*wlen:i+(j+1)*wlen]
                if subword in cntword:
                    seen[subword]=seen.get(subword,0)+1
                    # if word has seen bigger than target
                    if seen[subword]>cntword[subword]:
                        break
                else:
                    break
                j+=1
            if j==num:
                res.append(i)
        return res
        