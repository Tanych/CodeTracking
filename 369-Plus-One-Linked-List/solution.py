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
        
    def nomodify(self,head):
        node=head
        hascarry=False
        # record the consecuctive 9 start point
        spos=0
        idx=0
        # record the previous number
        pre=0
        while node:
            if node.val!=9:
                pre=0
            # find the first 9
            if pre!=9 and node.val==9:
                pre=9
                spos=idx
            if node.next is None and node.val==9:
                hascarry=True
            idx+=1
            node=node.next
        # if no carry update to max len
        if not hascarry:
            spos=idx
            
        # start update from the consecutive 9
        node=head
        idx=0
        while node:
            # 2-9-9 update from spos-1
            if spos-1<=idx:
                node.val=(node.val+1)%10
            idx+=1
            node=node.next
        # add the 1 for 9-9-9
        if hascarry and spos==0:
            newhead=ListNode(1)
            newhead.next=head
            head=newhead
        return head
        
        
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.nomodify(head)
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
        