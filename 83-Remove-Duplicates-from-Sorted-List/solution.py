# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        pre=head
        cur=head.next
        while cur:
            if cur.val==pre.val:
                if not cur.next:
                    pre.next=None
                    break
                else:
                    p=cur.next
                    pre.next=cur.next
                    cur=p
            else:
                pre=cur
                cur=cur.next
        return head