class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        t=m+n-1
        l1,l2=m-1,n-1
        while l1>=0 and l2>=0:
            if nums1[l1]>nums2[l2]:
                nums1[t]=nums1[l1] 
                l1-=1
            else:
                nums1[t]=nums2[l2]
                l2-=1
            t-=1
            
        # check whether nums2 is large part, no need to check nums1
        while l2>=0:
            nums1[t]=nums2[l2]
            t-=1
            l2-=1
        
        