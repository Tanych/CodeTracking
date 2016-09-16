class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n=len(nums)
        mid=nums[n/2]
        A=lambda i:(2*i+1)%(n|1)
        # tree way partion
        i,j,k=0,0,n-1
        while j<=k:
            if nums[A(j)]>mid:
                nums[A(i)],nums[A(j)]=nums[A(j)],nums[A(i)]
                i+=1
                j+=1
            elif nums[A(j)]<mid:
                nums[A(j)],nums[A(k)]=nums[A(k)],nums[A(j)]
                k-=1
            else:
                j+=1
                
        