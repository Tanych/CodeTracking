# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p,q=head,head.next
        dump=ListNode(-1)
        dump.next=head.next
        
        while q and q.next:
            p.next=q.next
            tmp=q.next
            q.next=q.next.next
            p=tmp
            q=tmp.next
            
        p.next=dump.next
        return head
            