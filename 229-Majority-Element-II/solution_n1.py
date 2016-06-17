class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        value = []
        count =[]
        res=[]
        n=len(nums)
        if n==0:
            return value
        for i in xrange(n):
            if len(value)==0:
                value.append(nums[i])
                count.append(1)
            elif len(value)==1:
                if nums[i]==value[0]:
                    count[0]+=1
                else:
                    value.append(nums[i])
                    count.append(1)
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
                        
        for i in xrange(len(value)):
            temp=0
            for j in xrange(n):
                if nums[j]==value[i]:
                    temp+=1
            if temp>n/3:
                res.append(value[i])
        return res
        