# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head):
        if not head or not head.next:
            return head
            
        pre=None
        cur=head
        while cur:
            # record the value before it change
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        return pre
    
    def partionlist(self,head):
        if not head or not head.next:
            return head
        slow=head
        fast=head.next.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        # make sure the left is 1 more than right part if odd
        if fast:
            fast=slow.next.next
            slow.next.next=None
        else:
            fast=slow.next
            slow.next=None
        return fast
        
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # first partion list
        right=self.partionlist(head)
        # reverse the right part
        reverse=self.reverse(right)
        
        p=head
        q=reverse
        while p and q:
            # record the next possible value
            nextp=p.next
            nextq=q.next
            # change the link
            p.next=q
            q.next=nextp
            # move on
            p=nextp
            q=nextq
  
        
        