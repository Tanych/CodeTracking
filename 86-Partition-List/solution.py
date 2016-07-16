# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # find the first element that >=x
        if not head or not head.next:
            return head
            
        newhead=ListNode(-1)
        newhead.next=head
        bigpre=newhead
        bigcur=head
        
        while bigcur:
            if bigcur.val>=x:
                break
            bigpre=bigcur
            bigcur=bigcur.next
        # not find return
        if not bigcur:
            return head
            
        smallpre=None
        smallcur=bigcur
        while smallcur:
            if smallcur.val<x:
                pnext=smallcur.next
                bigpre.next=smallcur
                smallcur.next=bigcur
                smallpre.next=pnext
                bigpre=smallcur
                smallcur=pnext
            else:
                smallpre=smallcur
                smallcur=smallcur.next
        
        return newhead.next
        
        