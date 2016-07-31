class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        It's a problem with bucket sort.Also, we should
        has some idea of math.
        Assume the min of the array is A, and the max is B
        the min of the gap would be make all the gap equal,
        otherwise, if some gets smaller other gaps would be larger.
        So, the bucket length would be ceiling((B-A)/(N-1))
        and the maxium bucket numer is (B-A)/bucketlen+1
        some of the bucket would be empty
        """
        n=len(nums)
        if n<2: return 0
        min_num=min(nums)
        max_num=max(nums)
        
        # the math ceil might influence the efficency
        #bucket_range=max(1,int(math.ceil((max_num-min_num)/(n-1))))
        bucket_range=max(1,int((max_num-min_num-1)/(n-1))+1)
        bucket_len=(max_num-min_num)/bucket_range+1
        buckets=[None]*bucket_len
        
        # adding to buckets
        for num in nums:
            pos=(num-min_num)/bucket_range
            t_bucket=buckets[pos]
            if not t_bucket:
                # record the min and max
                t_bucket={'min':num,'max':num}
                buckets[pos]=t_bucket
            else:
                # update min and max
                t_bucket['min']=min(t_bucket['min'],num)
                t_bucket['max']=max(t_bucket['max'],num)
        # get the possible maxgap
        # using the n.min-(n-1).max 
        res=0
        for i in xrange(bucket_len):
            # get rid of the empty
            if not buckets[i]:
                continue
            j=i+1
            # get rid the continue j is empty
            # EX NULL,[1,2],NULL,NULL,[4,5]
            while j<bucket_len and not buckets[j]:
                j+=1
            # get the max gap
            if j<bucket_len:
                res=max(res,buckets[j]['min']-buckets[i]['max'])
            i=j
            
        return res
            
        