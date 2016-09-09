class Solution(object):
    def majortyElementK(self, nums,k):
        cntmap,res={},[]
        if k<2: return res
        n=len(nums)
        if not n: return res
        for i in xrange(n):
            if len(cntmap)<k-1:
                cntmap[nums[i]]= cntmap.get(nums[i],0)+1
            else:
                if nums[i] in cntmap:
                    cntmap[nums[i]]+=1
                    continue
                find=False
                for key in cntmap:
                    if cntmap[key]==0:
                        del cntmap[key]
                        cntmap[nums[i]]= cntmap.get(nums[i],0)+1
                        find=True
                        break
                # if not cnt==0, all decrease one
                if not find:
                    for key in cntmap:
                        cntmap[key]-=1
        print cntmap
        # check the final
        res=[n for n in cntmap if nums.count(n)>(len(nums)/k)]
        return res
            
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.majortyElementK(nums,3)
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
        