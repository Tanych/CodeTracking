class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        the easiest way to solve the problem is divide and conque
        when we do the merge we should be careful about the same height merge in,
        we should aviod this situaiton
        we need set a vaule to record the maxHeight merged
        """
        n=len(buildings)
        if n==0:
            return []
        res=[]    
        return self.divide(0,n-1,buildings)
        
    def divide(self,start,end,buildings):
        res=[]
        #divide to one
        if start==end:
            res.append([buildings[start][0],buildings[start][2]])
            res.append([buildings[start][1],0])
            return res
        #else, do the divide and conque
        mid=(end+start)/2
        left=self.divide(start,mid,buildings)
        right=self.divide(mid+1,end,buildings)
        res=self.conque(left,right)
        return res
    
    def conque(self,left,right):
        i=j=h1=h2=0
        res=[]
        while i<len(left) and j<len(right):
            #if the x bigger
            if left[i][0]<right[j][0]:
                h1=left[i][1]
                x=left[i][0]
                i+=1
            elif left[i][0]>right[j][0]:
                h2=right[j][1]
                x=right[j][0]
                j+=1
            else:
                h1=left[i][1]
                h2=right[j][1]
                x=left[i][0]
                j+=1
                i+=1
            newp=[x,max(h1,h2)]
            if not res or res[-1][1]!=newp[1]:
                res.append(newp)
        #add the left
        while i<len(left):
            res.append(left[i])
            i+=1
        while j<len(right):
            res.append(right[j])
            j+=1
        return res
        