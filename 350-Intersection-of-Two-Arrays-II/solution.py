class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1=len(nums1)
        n2=len(nums2)
        map1={}
        map2={}
        
        res=[]
        # building map for the nums2
        for i in xrange(n1):
            map1[nums1[i]]=map1.get(nums1[i],0)+1
               
        for i in xrange(n2):
            map2[nums2[i]]=map2.get(nums2[i],0)+1
        
        keys_intersect=set(map1.keys()) & set(map2.keys())
        
        for key in keys_intersect:
            cnt=min(map1[key],map2[key])
            res+=[key for _ in xrange(cnt)]
            
        return res