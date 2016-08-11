class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        EXAMPLE:
        6 8 7 4 3 2
        (6)  8 7 4 3 2
        6 8 (7) 4 3 2
        7 8 6 4 3 2
        7 2 3 4 6 8
        """
        num_len=len(nums)
        for j in xrange(num_len-1,-1,-1):
            #find the first larg ele than the pre one
            if j>0 and nums[j]>nums[j-1]:
                #if it's the last one, swap
                if j==num_len-1:
                    nums[j],nums[j-1]=nums[j-1],nums[j]
                    break
                #if not ,we need find the the larger ele in j--num_len
                for k in xrange(num_len-1,j-1,-1):
                    if nums[k]>nums[j-1]:
                        nums[k],nums[j-1]=nums[j-1],nums[k]
                        break
                #finally reversed the rest
                nums[j:]=nums[j:][::-1]
                break
            if j==0:
                nums.reverse()
        