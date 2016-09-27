# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummpy=ListNode(-1)
        dummpy.next=head
        slow=dummpy
        fast=dummpy
        # reach on the n node from left
        for i in xrange(n):
            fast=fast.next
        # slow reach on the n-1 node from right
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummpy.next