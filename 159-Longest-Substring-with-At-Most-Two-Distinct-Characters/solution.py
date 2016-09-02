class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=end=0
        cnt=[0]*128
        count=res=0
        while end<len(s):
            if cnt[ord(s[end])]==0:
                count+=1
            cnt[ord(s[end])]+=1
            end+=1
            while count>2:
                if cnt[ord(s[start])]==1:
                    count-=1
                cnt[ord(s[start])]-=1
                start+=1
            res=max(res,end-start)
        return res