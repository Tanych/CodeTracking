# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.res=[]
        
    def printnode(self,start,end):
        if start==end:
            return
        if start.next==end:
            # deal with end point the last element but not none
            #if end and not end.next:
            #    self.res.append(end.val)
            self.res.append(start.val)
            return
        if start.next.next==end:
            # deal with end point the last element but not none
            #if end and not end.next:
            #    self.res.append(end.val)
            self.res.append(start.next.val)
            self.res.append(start.val)
            return
        
        slow=start
        fast=start
        while fast!=end:
            slow=slow.next
            fast=fast.next.next if fast.next!=end else end
            
        #print start.val,end.val,slow.val,fast.val
        
        self.printnode(slow,fast)
        self.printnode(start,slow)
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return self.res
        if not head.next:
            self.res.append(head.val)
            return self.res
        slow=head
        fast=head
        while fast:
            slow=slow.next
            fast=fast.next.next if fast.next else None
        #print slow.val,fast.val
        self.printnode(slow,fast)
        self.printnode(head,slow)
        return self.res
        