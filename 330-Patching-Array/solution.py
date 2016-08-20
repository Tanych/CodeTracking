class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        """
        if the array can represent[1,total)
        when I add to the element add, it can be represent the way of [1,total+add)
        if num <total, we use the number alway in the num,
        if not we add to the number
        1-2^n can combine any number in n number
        """
        
        added=0
        #the total of the number less the
        miss=1
        #index of the num
        i=0
        size=len(nums)
        while miss<=n:
            #if the number less than the total,we use the number alway in the array
            # that we can [1,num[i]+miss)
            if i<size and nums[i]<=miss:
                miss+=nums[i]
                i+=1
            #if not we expand to check [1,2*miss)
            else:
                miss+=miss
                added+=1
        return added
        