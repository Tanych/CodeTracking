# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        
        pre=None
        cur=head
        
        while cur:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
            
        return pre