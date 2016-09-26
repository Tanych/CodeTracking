# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
        cnt=0
        dummy=ListNode(-1)
        dummy.next=head
        cur=dummy
        while cnt<m-1:
            cur=cur.next
            cnt+=1
        # now cur get the m-1 node
        p=cur.next
        while cnt<n-1:
            tmp=p.next
            p.next=tmp.next
            tmp.next=cur.next
            cur.next=tmp
            cnt+=1
        return dummy.next
            
        
        
        