# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        p=head
        hashmap={}
        
        while p:
            if p in hashmap:
                return p
            else:
                hashmap[p]=hashmap.get(p,0)+1
            p=p.next
            
        return None