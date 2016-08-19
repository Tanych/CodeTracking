# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def lreverse(self,head):
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
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # the O(1) space is difficult
        # first divide the linked list into two part
        # reverse the left part 
        # and then compare the two part
        
        # divide into two part
        if not head:
            return True
        if not head.next:
            return True
            
        # step1--divide;slow move 1 fast move double
        slow=head
        fast=head.next.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        # 1-2-3-3-2-1===>1-2-3(slow) 3(fast)-2-1
        # 1-2-1====1(slow)-2(fast)-1
        # the right part might 1 more than left
        if not fast:
            fast=slow.next
        else:
            fast=slow.next.next
            
        slow.next=None
        
        # step2: reverse left part
        reverse=self.lreverse(head)
        
        while fast:
            if reverse.val!=fast.val:
                return False
            reverse=reverse.next
            fast=fast.next
        
        return True
        
        
        
        
        