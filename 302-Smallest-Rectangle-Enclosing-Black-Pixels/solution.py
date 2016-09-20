class Solution(object):
    def searchrows(self,image,start,end,istop):
        while start<end:
            mid=(start+end)/2
            if ('1' in image[mid])==istop:
                end=mid
            else:
                start=mid+1
        return start
        
    def searchcols(self,image,start,end,top,bottom,isleft):
        while start<end:
            mid=(start+end)/2
            if any('1'==image[k][mid] for k in xrange(top,bottom))==isleft:
                end=mid
            else:
                start=mid+1
        return start
        
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        top = self.searchrows(image, 0, x, True)
        bottom = self.searchrows(image, x + 1, len(image), False)
        left = self.searchcols(image, 0, y, top, bottom, True)
        right = self.searchcols(image, y + 1, len(image[0]), top, bottom, False)
        return (bottom - top) * (right - left)
        