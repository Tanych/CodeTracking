# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self,head):
        pre,cur=None,head
        while cur:
            nextp=cur.next
            cur.next=pre
            pre=cur
            cur=nextp
        return pre
        
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        carry=1
        newhead=self.reverse(head)
        cur=newhead
        while cur:
            cur.val,carry=(cur.val+carry)%10,(cur.val+carry)/10
            cur=cur.next
        
        res=self.reverse(newhead)
        if carry:
            node=ListNode(1)
            node.next=res
            return node
        else:
            return res
        