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
        # use bucket to store the same frequency key
        bucket=[[] for _ in xrange(n+1)]
        # building map
        for i in xrange(n):
            hashmap[nums[i]]=hashmap.get(nums[i],0)+1
        
        # sort map by value
        for key,value in hashmap.iteritems():
            bucket[value].append(key)
        # the index indicate the frequncy
        for i in xrange(len(bucket)-1,-1,-1):
            if len(res)<k and bucket[i]:
                res+=bucket[i]
        return res
