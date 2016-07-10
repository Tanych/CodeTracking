class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        start=-1
        end=0
        found=False
        left=0
        right=n-1
        for i in xrange(n):
            mid=left+(right-left)/2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                found=True
                start=mid
                while start>0:
                    if nums[start-1]==target:
                        start-=1
                    else:
                        break
                end=mid
                while end<n-1:
                    if nums[end+1]==target:
                        end+=1
                    else:
                        break
                        
        return [start,end] if found else [-1,-1]
        