# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, left, right):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummpy=ListNode(0)
        p=dummpy
        while left and right:
            if left.val<=right.val:
                p.next=left
                left=left.next
            else:
                p.next=right
                right=right.next
            p=p.next
        p.next=left if left else right
        return dummpy.next
        