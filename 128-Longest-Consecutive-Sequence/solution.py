class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea something like bucket sort, 
        # put the element n at the (start,end) bucket, everytime
        # check n-1 or n+1 in the bucket, if so combine them
        
        bucket={}
        max_len=1
        for num in nums:
            # duplicate n pass
            if bucket.has_key(num):
                continue
            # inital n.start n.end is itself
            start=end=num
            # if has n-1
            if bucket.has_key(num-1):
                # update the start to the n-1.start
                start=bucket[num-1][0]
            if bucket.has_key(num+1):
                # update the end to the n+1.end
                end=bucket[num+1][1]
            # add the update value to the bucket
            bucket[start]=bucket[end]=bucket[num]=(start,end)
            max_len=max(end-start+1,max_len)
        return max_len
        