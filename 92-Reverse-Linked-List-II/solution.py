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
        
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        if m==n:
            return head
        t=m
        mcur=head
        mpre=None
        while t>1:
            mpre=mcur
            mcur=mcur.next
            t-=1
        # get the firs part
        tlast1=mpre
        if mpre:
            mpre.next=None
        #print mcur.val
        
        npre=None
        ncur=mcur
        b=n
        while b>=m:
            npre=ncur
            ncur=ncur.next
            print n,m,npre.val
            b-=1
            
        # get the second part
        tlast2=npre
        #print npre.val
        #if not ncur:
        npre.next=None
        #print mcur.val
        
        rhead=self.reverselist(mcur)
        #print rhead.val
            
        # combine
        if tlast1:
            tlast1.next=rhead
        
        mcur.next=ncur
        
        return head if tlast1 else rhead
        
            
        
        
        