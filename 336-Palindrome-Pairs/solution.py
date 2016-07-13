class Solution(object):
    def ispalindrome(self,strs):
        l,r=0,len(strs)-1
        while l<r:
            if strs[l]!=strs[r]:
                return False
            l+=1
            r-=1
        return True
        
        
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n=len(words)
        res=[]
        # using the hash map record the reverse
        hashmap={}
        for i in xrange(n):
            hashmap[words[i][::-1]]=i
            
        # deal with empty case ""
        # if words[i] is palindrome, combine with empty is also true
        if "" in hashmap:
            for i in xrange(len(words)):
                if words[i]=="":
                    continue
                if self.ispalindrome(words[i]):
                    res.append([hashmap[""],i])
        
        for i in xrange(len(words)):
          for j in xrange(len(words[i])):
              # from left to right find the reverse key and self palindrome
              left=words[i][:j]
              right=words[i][j:]
              # if left has the reverse and check the right part
              if left in hashmap and self.ispalindrome(right) and hashmap[left]!=i:
                  res.append([i,hashmap[left]])
              # vice versa
              if right in hashmap and self.ispalindrome(left) and hashmap[right]!=i:
                  res.append([hashmap[right],i])
            
        return res
                