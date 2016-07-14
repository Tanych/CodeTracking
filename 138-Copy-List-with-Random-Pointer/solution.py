# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def dfs(self,hashmap,node):
        newnode=RandomListNode(node.label)
        hashmap[node]=newnode
        
        if node.random:
            if node.random not in hashmap:
                self.dfs(hashmap,node.random)
            hashmap[node].random=hashmap[node.random]
        if node.next:
            if node.next not in hashmap:
                self.dfs(hashmap,node.next)
            hashmap[node].next=hashmap[node.next]
        
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
            
        # map to search
        hashmap={}
        self.dfs(hashmap,head)
        return hashmap[head]
        