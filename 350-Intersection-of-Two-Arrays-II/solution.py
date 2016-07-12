class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1=len(nums1)
        n2=len(nums2)
        maping={}
        res=[]
        for i in xrange(n1):
            maping[nums1[i]]=maping.get(nums1[i],0)+1
        
        for i in xrange(n2):
            maping[nums2[i]]=maping.get(nums2[i],0)-1
            if maping[nums2[i]]>=0:
                res.append(nums2[i])
        return res