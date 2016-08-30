class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        strcnt=[0]*128
        res=cnt=left=right=0
        while right<len(s):
            if strcnt[ord(s[right])]==0:
                cnt+=1
            strcnt[ord(s[right])]+=1
            right+=1
            
            while cnt>k:
                if strcnt[ord(s[left])]==1:
                    cnt-=1
                strcnt[ord(s[left])]-=1
                left+=1
            res=max(res,right-left)
        return res
                