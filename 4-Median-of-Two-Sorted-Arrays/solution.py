class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        binsearch
        a1 a2 a3...a(n/2)...a(n) section1 section2
        b1 b2 b3...b(m/2)...b(m) section3 section4
        if m+n is even then k would be the number of [(m+n)/2,(m+n)/2+1]
        if m+b is odd then k would be (m+n)/2+1
        Rules:
        if (n/2+m/2)>k and a[n/2]>b[m/2]:
            drop section 2
        if (n/2+m/2)>k and a[n/2]<b[m/2]:
            drop section 4
        if (n/2+m/2)<k and a[n/2]<b[m/2]:
            drop section 1
        if (n/2+m/2)><k and a[n/2]>b[m/2]:
            drop section 3
        """
        def findkth(nums1,nums2,k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]
            
            midx1,midx2=len(nums1)/2,len(nums2)/2
            mnum1,mnum2=nums1[midx1],nums2[midx2]
            
            if (midx1+midx2)>=k:
                if mnum1>=mnum2:
                    # drop section 2
                    return findkth(nums1[:midx1],nums2,k)
                else:
                    # drop section 4
                    return findkth(nums1,nums2[:midx2],k)
            else:
                if mnum1>=mnum2:
                    # drop section 3
                    return findkth(nums1,nums2[midx2+1:],k-midx2-1)
                else:
                    # drop section 1
                    return findkth(nums1[midx1+1:],nums2,k-midx1-1)
                
                
        l=len(nums1)+len(nums2)
        if not l%2:
            m1=findkth(nums1,nums2,l/2)
            m2=findkth(nums1,nums2,l/2-1)
            return (m1+m2)/2.0
        else:
            return findkth(nums1,nums2,l/2)
            