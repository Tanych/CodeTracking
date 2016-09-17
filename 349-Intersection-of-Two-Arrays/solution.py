class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        mapping={}
        for num in nums1:
            mapping[num]=mapping.get(num,0)+1
        
        for num in nums2:
            if num in mapping:
                res.append(num)
                del mapping[num]
        return res