class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The max number of majority element of n/k is k-1
        # the value, count maxium is 2, so it's O(1)
        value = []
        count =[]
        res=[]
        n=len(nums)
        if n==0:
            return value
        for i in xrange(n):
            # if empty, insert 
            if len(value)==0:
                value.append(nums[i])
                count.append(1)
            # if one, check whether equal 
            elif len(value)==1:
                if nums[i]==value[0]:
                    count[0]+=1
                else:
                    value.append(nums[i])
                    count.append(1)
            # if two, check 2 of them and delete the count is 0 
            else:
                if nums[i]==value[0]:
                    count[0]+=1
                elif nums[i]==value[1]:
                    count[1]+=1
                else:
                    count[0]-=1
                    count[1]-=1
                    if count[1]==0:
                        del value[1]
                        del count[1]
                    if count[0]==0:
                        del value[0]
                        del count[0]
        # filter the value
        for i in xrange(len(value)):
            cnt=0
            for j in xrange(n):
                if nums[j]==value[i]:
                    cnt+=1
            if cnt>n/3:
                res.append(value[i])
        return res
        