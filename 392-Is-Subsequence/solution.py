class Solution(object):
    def isSubsequence1(self, s, t):
        # create a list to save the index of each letter in t
        listt = [[] for _ in range(26)]
        
        for i in range(len(t)):
            listt[ord(t[i])- 97].append(i)
        # create a list to find the index of each letter of s in t    
        lists = [0 for _ in range(len(s))]
        
        if not s: return True
        if not listt[ord(s[0])-97]: return False # if first letter of s is not in t
        lists[0] = listt[ord(s[0])-97].pop(0) # min. value for first letter
                
        for i in range(1,len(s)):
            if not listt[ord(s[i])-97]: return False # if the letter is not in t
            index, value = self.helper(listt[ord(s[i])-97],lists[i-1])
            if index == -1: return False
            lists[i],listt[ord(s[i])-97]= value, listt[ord(s[i])-97][index+1:]
                    
        return lists == sorted(lists)
      # a helper function to find the index   
    def helper(self, nums, value):
        if value > nums[-1]: return (-1,-1)
        else:
            temp, i = nums[0], 0
            while value > temp and i < len(nums):
                i+=1
                temp = nums[i]
        return (i,temp)
        
    def manys(self,s,t):
        hmaping=[[] for _ in range(26)]
        # pre record the position
        for i in xrange(len(t)):
            hmaping[ord(t[i])- 97].append(i)
        
        # search index
        curidx=-1
        for ch in s:
            if not hmaping[ord(ch)-97] or hmaping[ord(ch)-97][-1]<=curidx:
                return False
            left,right=0,len(hmaping[ord(ch)-97])-1
            while left<right:
                mid=(left+right)/2
                if hmaping[ord(ch)-97][mid]>curidx:
                    right=mid
                else:
                    left=mid+1
            curidx=hmaping[ord(ch)-97][left]
        return True
                
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.manys(s,t)
        sidx=tidx=0
        while sidx<len(s) and tidx<len(t):
            if s[sidx]==t[tidx]:
                sidx+=1
            tidx+=1
        return sidx==len(s)
        
        i=0
        for ch in s:
            newi=t.find(ch,i)
            if newi==-1:return False
            i=newi+1
        return True