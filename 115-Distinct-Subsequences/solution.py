class Solution(object):
     def helper(self,s, t, hashmap={}):
        res=0
        if not t:           
            return 1
        if not s and t:     
            return 0
        # if already searched return the result
        if (s, t) in hashmap:  
            return hashmap[s, t]
        # try to find the possible count in the laster string
        for i in range(len(s)):
            if t[0] == s[i]: 
                res += self.helper(s[i+1:], t[1:], hashmap)
        
        hashmap[s,t] = res
        return hashmap[s,t]
        
     def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return self.helper(s,t)