# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
            return None
        # deal the one in first ele
        while(head != None and head.val == val):
            head = head.next
        if head==None:
            return None
        # pre, curr
        p,q=head,head.next
        while q!=None:
            # if has the val, del
            while q.val==val:
                # mov next
                p.next=q.next
                if q.next==None:
                    return head
                q=q.next
            # no del mov next
            p,q=q,q.next
        return head
            
        