# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # the discription of the question need more
        # details since 1-2-3-2-1 4-1-2-4-5 is not possible
        # only the intersection can happend in the end
        
        sizeA,sizeB=0,0
        # get the length
        p=headA
        while p:
            sizeA+=1
            p=p.next
        p=headB
        while p:
            sizeB+=1
            p=p.next
        # get rid of the not equal len        
        curA=headA
        while sizeA>sizeB:
            sizeA-=1
            curA=curA.next
        curB=headB
        while sizeB>sizeA:
            sizeB-=1
            curB=curB.next
            
        # compare
        while curA!=curB:
            curA=curA.next
            curB=curB.next
        
        return curA