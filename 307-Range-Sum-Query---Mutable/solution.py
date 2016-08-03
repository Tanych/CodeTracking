class SegmentTreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None


class SegmentTree(object):
    def __init__(self, nums):
        """
        Initial the segment Tree for the given list nums
        :param nums:
        :return:
        """
        self.num_len = len(nums)
        self.__root = self._build_seg_tree(nums, 0, self.num_len - 1)

    def update(self, pos, val):
        self._update_seg_tree(self.__root, pos, val)

    def sumrange(self, start, end):
        return self._sumrange_seg_tree(self.__root, start, end)

    def _build_seg_tree(self, nums, start, end):
        """
        build a segment tree with divide and conquer
        :param nums: the number lists
        :param start: the range start position
        :param end: the range end position
        :return: the root of the segment tree
        """
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        # if only one node
        if start == end:
            root.sum = nums[start]
        else:
            mid = start + (end - start) / 2
            # get the left sum range
            root.left = self._build_seg_tree(nums, start, mid)
            # get the right sum range
            root.right = self._build_seg_tree(nums, mid + 1, end)
            root.sum = root.left.sum + root.right.sum
        return root

    def _update_seg_tree(self, root, pos, val):
        """
         Update the value in the special position
        :param root: the node of segment tree
        :param pos: the update position
        :param val: the update value
        :return: None
        """
        # find only one node
        if root.start == root.end:
            root.sum = val
        else:
            mid = root.start + (root.end - root.start) / 2
            # if the pos on the left branch range
            if pos <= mid:
                self._update_seg_tree(root.left, pos, val)
            else:
                self._update_seg_tree(root.right, pos, val)
            # update the sum
            root.sum = root.left.sum + root.right.sum

    def _sumrange_seg_tree(self, root, start, end):
        """

        :param root:
        :param start:
        :param end:
        :return:
        """
        if root.start == start and root.end == end:
            return root.sum
        else:
            mid = root.start + (root.end - root.start) / 2
            # if the range totally on the left branch
            if end <= mid:
                return self._sumrange_seg_tree(root.left, start, end)
            # if the range totally on the right branch
            elif start >= mid + 1:
                return self._sumrange_seg_tree(root.right, start, end)
            # otherwise, get the two parts
            else:
                return self._sumrange_seg_tree(root.left, start, mid) + \
                       self._sumrange_seg_tree(root.right, mid + 1, end)
                 
    
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.__root = SegmentTree(nums)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.__root.update(i,val)
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.__root.sumrange(i, j)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)