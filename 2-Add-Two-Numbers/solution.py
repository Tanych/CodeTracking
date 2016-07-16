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
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l1:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        carry=0
        newhead=ListNode(-1)
        p=newhead
        
        while l1 and l2:
            sumval=l1.val+l2.val+carry
            tval=sumval%10
            carry=sumval/10
            p.next=ListNode(tval)
            p=p.next
            l1=l1.next
            l2=l2.next
        
        while l1:
            if carry:
                sumval=l1.val+carry
                tval=sumval%10
                carry=sumval/10
                p.next=ListNode(tval)
            else:
                p.next=ListNode(l1.val)
            p=p.next
            l1=l1.next
        
        while l2:
            # make sure the previous carry
            if carry:
                sumval=l2.val+carry
                tval=sumval%10
                carry=sumval/10
                p.next=ListNode(tval)
            else:
                p.next=ListNode(l2.val)
            p=p.next
            l2=l2.next
        # keep the last carry
        if carry:
            p.next=ListNode(carry)
        
        return newhead.next
        
        