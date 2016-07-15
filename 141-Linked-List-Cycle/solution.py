# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        # Tortoise and hare
        # using two diffirent pointer with two different speed
        # if has the cycle if could equal
        slow=head
        fast=head.next.next
        try:
            while slow is not fast:
                slow=slow.next
                fast=fast.next.next
            # if match
            return True
        except:
            return False