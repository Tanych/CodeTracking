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
            
        #record the lengt of two parts
        lenp1,lenp2=m,n
        
        # divide the first part
        mcur=head
        mpre=None
        while lenp1>1:
            mpre=mcur
            mcur=mcur.next
            lenp1-=1
        # get the firs part
        plast1=mpre
        # deal with the head case
        if mpre:
            mpre.next=None
        
        # divide the second part
        npre=None
        ncur=mcur
        while lenp2>=m:
            npre=ncur
            ncur=ncur.next
            lenp2-=1
        npre.next=None
        
        # reverse m--n part
        # mcur is the start point of m
        rhead=self.reverselist(mcur)
            
        # concat the part1 and reverse part
        if plast1:
            plast1.next=rhead
        # concat the end of reverse part and third part
        mcur.next=ncur
        
        return head if plast1 else rhead
        
            
        
        
        