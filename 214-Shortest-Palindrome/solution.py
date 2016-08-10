class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Find the max length of palindom start from 0, and add the reverse part in the previous
        
        The smartest way to solve this problem is combine kmp and reverse
        reverse the string and combine them, we only need to check the last pre of the combine string
        then we minus the largest pre and comnie them
        EX:
        aacecaaa#aaacecaa
        we only care about the last letter of the in the pre array
        """
        if not s:
            return ""
            
        #initial build the string
        revs=s[::-1]
        new_str=s+'#'+revs
        #mark the next array in KMP
        next=[0]*(len(new_str)+1)
        j=0
        for i in xrange(1,len(new_str)):
            #if not equal,we check back the first equal string
            while j>0 and new_str[i]!=new_str[j]: j=next[j]
            if new_str[i]==new_str[j]:j+=1
            next[i+1]=j
        return revs[:len(s)-next[-1]]+s
        
        