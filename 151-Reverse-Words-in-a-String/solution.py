class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        words=s.split()
        print words
        i,j=0,len(words)-1
        while i<j:
            words[i],words[j]=words[j],words[i]
            i+=1
            j-=1
        resstr=''
        for word in words:
            resstr+=word+' '
            
        return resstr.strip()
        
            