# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        newhead=ListNode(-2<<31-1)
        newhead.next=head
        prepre=newhead
        pre=head
        cur=head.next
        
        while cur:
            if not cur.next:
                prepre.next=cur
                cur.next=pre
                pre.next=None
                break
            p=cur.next
            prepre.next=cur
            cur.next=pre
            pre.next=p
            cur=p.next
            prepre=pre
            pre=p
            
        return newhead.next
            
            
        