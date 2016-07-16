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
        # get the size of head
        if not head:
            return None
        if not head.next:
            if n==1:
                return None
        p=head
        sizehead=0
        while p:
            sizehead+=1
            p=p.next
        
        steps=sizehead-n
        newhead=ListNode(-1)
        newhead.next=head
        pre=newhead
        cur=head
        while steps:
            pre=cur
            cur=cur.next
            steps-=1
        # record the next possible valu
        cnext=cur.next
        pre.next=cnext
        
        return newhead.next
        
        