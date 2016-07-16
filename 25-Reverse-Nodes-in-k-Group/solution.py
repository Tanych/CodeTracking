# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverselist(self,head):
        if not head or not head.next:
            return head
        pre=None
        cur=head
        while cur:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        return pre
        
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k==1:
            return head
    
        newhead=ListNode(-1)
        newhead.next=head
        prepre=newhead
        pre=head
        cur=head
        steps=k-1
        while cur:
            while cur.next and steps:
                cur=cur.next
                steps-=1
            # if steps not enough break
            if steps:
                break
            # record the cur next
            #print pre.val,cur.val
            pnext=cur.next
            cur.next=None
            rhead=self.reverselist(pre)
            #print rhead.next.val
            prepre.next=rhead
            pre.next=pnext
            prepre=pre
            pre=pnext
            cur=pnext
            steps=k-1
        
        return newhead.next