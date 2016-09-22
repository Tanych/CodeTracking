class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.res_list=[]
        self.res_list.extend([li for li in vec2d])
        

    def next(self):
        """
        :rtype: int
        """
        return self.res_list[0].pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.res_list)==0:
            return False
            
        while self.res_list and not self.res_list[0]:
                self.res_list.pop(0)
        return not len(self.res_list)==0

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())