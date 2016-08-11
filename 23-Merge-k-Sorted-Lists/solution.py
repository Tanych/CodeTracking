# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        
        minheap=[]
        #pre-work  build a min heap
        for node in lists:
            if node:
                heapq.heappush(minheap, (node.val,node))
        
        dumpy=ListNode(0)
        p=dumpy
        while minheap:
            #get the min of the heap
            val,peek=heapq.heappop(minheap)
            #save the value
            p.next=ListNode(val)
            p=p.next
            #add the smallest next node to the min heap
            if peek.next:
                heapq.heappush(minheap,(peek.next.val,peek.next))

        return dumpy.next
        