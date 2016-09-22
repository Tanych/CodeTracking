class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        n,hashmap=len(s),{}
        if n==1:
            return True
        for ch in s:
            hashmap[ch]=hashmap.get(ch,0)+1
            
        if len(hashmap)==1:
            return True
        num_odd = 0
        for ch in hashmap:
            if hashmap[ch]%2!=0:
                num_odd+=1
        if num_odd==0 or num_odd==1:
            return True
        return False
        
        
        