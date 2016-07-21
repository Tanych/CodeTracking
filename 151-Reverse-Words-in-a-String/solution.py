class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        #using split to get the words
        words=s.split()
        # two pointer to get the reverse
        i,j=0,len(words)-1
        while i<j:
            words[i],words[j]=words[j],words[i]
            i+=1
            j-=1
        resstr=''
        for word in words:
            resstr+=word+' '
            
        return resstr.strip()
        
            