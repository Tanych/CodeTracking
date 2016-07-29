class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n1,n2=len(nums1),len(nums2)
        heapsum=[]
        # push (i,j) into heap
        def hppush(i,j):
            if i<n1 and j<n2:
                heapq.heappush(heapsum,(nums1[i]+nums2[j],i,j))
        # push the smallest into 
        hppush(0,0)
        
        res=[]
        while heapsum and len(res)<k:
            # k might out of boundary
                _,idx1,idx2=heapq.heappop(heapsum)
                res.append([nums1[idx1],nums2[idx2]])
                # push the next smallest into heap
                hppush(idx1,idx2+1)
                # next to judge whether the smallest start from nums2 first ele
                # ex [1,2,3] [4,5,6] first add(5,1,4) and(6,1,5), also (6,2,4)
                # when the third pop (6,2,4) we consider add (7,3,4) into the heap
                if idx2==0:
                    hppush(idx1+1,0)
                
        return res