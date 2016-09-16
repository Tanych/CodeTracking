class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # two pointer
        left=right=min_len=0
        num_len=len(nums)
        cur_sum=nums[0] if nums else 0
        while right<num_len:
            while cur_sum<s:
                right+=1
                # if reach the boundary return
                if right==num_len:
                    return min_len
                cur_sum+=nums[right]
            if (right-left+1)<min_len or not min_len:
                min_len=right-left+1
            # update left, kick the most left ele
            cur_sum-=nums[left]
            left+=1
        return min_len
        