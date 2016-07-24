class Solution(object):
    
    def longestincresing(self,nums):
        n=len(nums)
        if n==0:
            return 0
        res=[nums[0]]
        for i in xrange(1,n):
            if nums[i]>res[-1]:
                res.append(nums[i])
            else:
                # try to find the value more closer to nums[i]
                #pos=bisect.bisect_left(res, nums[i])
                left,right=0,len(res)
                while left<right:
                    mid=(left+right)/2
                    if res[mid]==nums[i]:
                        left=mid
                        break
                    # take care the right--mid
                    if res[mid]>nums[i]:
                        right=mid
                    else:
                        left=mid+1
                res[left]=nums[i]
        return len(res)
        
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        # first sorting as width and count the increasin height
        # if width are equal sorting with height
        # since [[2, 3], [5, 4], [6, 4], [6, 7]]
        # the [6,4 ] has intersection between two parts
        # we need get the largest as possible
        envelopes=sorted(envelopes,lambda x,y:x[0]-y[0] if x[0]!=y[0] else y[1]-x[1])
        #print envelopes
        #get the height
        height=[]
        for i in xrange(len(envelopes)):
                height.append(envelopes[i][1])
        
        return self.longestincresing(height)
        