class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
            
        """
        the last diff is positive of the LWS
        and the last num can be or can't be nums[i]
        """
        positive=[0 for _ in xrange(n)]
        # the last diff is negative
        negative=[0 for _ in xrange(n)]
        # initial state
        positive[0]=1
        negative[0]=1
        for i in xrange(1,n):
            if nums[i]>nums[i-1]:
                """
                for the situation it's only possible for 
                positive get larger
                if the last num in down[i-1] is N
                if N>nums[i], replace N with num[i-1]
                if N<nums[i], add nums[i] to the subquence
                All equal make positive+1
                Also, it's imposible to make negative larger
                it can be prove by contridiction
                it could nums[i]<N then nums[i-1]<N
                it means we already use nums[i-1] be the element in negtive
                also nums[i-1] can't be N since nums[i]>nums[i-1]
                """
                positive[i]=negative[i-1]+1
                negative[i]=negative[i-1]
            elif nums[i]<nums[i-1]:
                negative[i]=positive[i-1]+1
                positive[i]=positive[i-1]
            else:
                positive[i]=positive[i-1]
                negative[i]=negative[i-1]
                
        return max(negative[-1],positive[-1])
        