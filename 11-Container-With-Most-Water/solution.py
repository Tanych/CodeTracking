class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # using two pointer to find possibilities
        maxarea = 0
        area = 0
        left_width, right_width = 0, len(height)-1

        while left_width < right_width:
            left_height, right_height = height[left_width], height[right_width]
            # if the left < right
            if left_height < right_height:
                area = (right_width-left_width)*left_height
                # turn right find another possibility
                while left_height >= height[left_width]:
                    left_width += 1
            else:
                area = (right_width-left_width)*right_height
                # turn left find another possibility, check the boundary to 0
                while right_height >= height[right_width] and right_width:
                    right_width -= 1
            if area > maxarea:
                maxarea = area
        return maxarea
        