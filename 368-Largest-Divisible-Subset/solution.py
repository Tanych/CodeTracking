class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap={-1:set()}
        for num in sorted(nums):
            # set combine
            # if num is the mutip of key then num is the mutip of all the ele
            # in the map
            maxdidlen=0
            maxkey=-1
            for key in hashmap:
                if num%key==0:
                    if len(hashmap[key])>maxdidlen:
                        maxdidlen=len(hashmap[key])
                        maxkey=key
            hashmap[num]=hashmap[maxkey]|{num}
            #hashmap[num]=max((hashmap[key] for key in hashmap if num%key==0),key=len)|{num}
        #print hashmap
        return list(max(hashmap.values(),key=len))