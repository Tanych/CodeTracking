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
        # make a cycle and break at the n-k-2
        if not head:
            return []
        length=1
        curr=head
        
        # get the list length
        while curr.next:
            length+=1
            curr=curr.next
        # make the list cycle
        curr.next=head
        k =k % length
        
        # search the stop position
        for i in xrange(length-k-1):
            head=head.next
        
        # get the n-k-2 
        stop=head
        # get the n-k-1
        head=head.next
        # since the head is a cycle, break at stop
        stop.next=None
        return head
        
        
        