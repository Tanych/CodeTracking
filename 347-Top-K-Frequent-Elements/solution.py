class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(nums)
        hashmap={} 
        res=[]
        # building map
        for i in xrange(n):
            hashmap[nums[i]]=hashmap.get(nums[i],0)+1
        
        # sort map by value
        cnt=0
        for key, value in sorted(hashmap.iteritems(), key=lambda (k,v): (v,k),reverse=True):
            if cnt<k:
                res.append(key)
                cnt+=1
        return res
