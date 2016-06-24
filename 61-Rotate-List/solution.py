# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k<=0:
            return head
        n=self.getlen(head)
        if n==0:
            return head
        k, end = k % n, n-1
        self.reverse(head,0, end-k)
        self.reverse(head,end-k+1,end)
        self.reverse(head,0,end)
        return head

    def getlen(self, head):
        nlen=0
        p=head
        if not p:
            return nlen
        nlen=1
        while p.next:
            nlen += 1
            p=p.next
        return nlen

    def getPos(self,head,pos):
        p=head
        if pos==0:
            return p
        while pos>0:
            p=p.next
            pos-=1
        return p

    def reverse(self,head,start,end):
        while start<end:
            # swap
            self.getPos(head,start).val, self.getPos(head,end).val= self.getPos(head,end).val, self.getPos(head,start).val
            # continue
            start+=1
            end-=1
            