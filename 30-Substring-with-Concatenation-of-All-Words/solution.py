class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        word_len=len(words[0])
        total_len=len(words)*word_len
        # building map for words
        res=[]
        i=0
        while i+total_len<=len(s):
            j=i
            found=True
            hashmap={}
            # reset the hashmap every trial
            for word in words:
                hashmap[word]=hashmap.get(word,0)+1
                
            while j< i+total_len:
                # if not in the hash, break
                if s[j:word_len+j] not in hashmap:
                    found=False
                    break
                else:
                    # if find than check whether occurs before
                    if hashmap[s[j:word_len+j]]<=0:
                        found=False
                        break
                    # no, update the occurs
                    hashmap[s[j:word_len+j]]-=1
                j+=word_len
            # if all in hashmap and only occurs once, add to res
            if found:
                res.append(i)
            i+=1
        return res