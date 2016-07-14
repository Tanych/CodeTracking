class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # using the template to sovle the substing question
        # it uses two pointer to find the substring
        
        start,end,count,max_len=0,0,0,0
        # record for all possible ASCII
        hashmap=[0]*128
        
        while end<len(s):
            # if repeat occurs, plus the count
            if hashmap[ord(s[end])]>0:
                count+=1
            hashmap[ord(s[end])]+=1
            end+=1
            # if has repeat, move the start
            while count>0:
                # if reaches the repeat the repeat num, decrease the count
                if hashmap[ord(s[start])]>1:
                    count-=1
                # also decrease the map
                hashmap[ord(s[start])]-=1 
                start+=1
            # if count==0 no repeat, get the max len
            max_len=max(max_len,end-start)
        return max_len
                    
            