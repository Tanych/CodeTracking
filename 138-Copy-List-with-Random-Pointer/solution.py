# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def printList(self,head):
        r=head
        while r!=None:
            print r.label,r.next,r.random
            r=r.next

    def searchNodeidx(self,head,node):
        p=head
        idx=0
        while p!=None:
            if node.label==p.label and node.next==p.next and node.random==p.random:
                return idx
            idx+=1
            p=p.next

    def searchNode(self,head,idx):
        p=head
        while idx>0:
            p=p.next
            idx-=1
        return p

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
            
        p=head
        copyrdm=RandomListNode(head.label)
        q=copyrdm
        while p.next!=None:
            # next copy
            q.next=RandomListNode(p.next.label)
            # move on for the next
            q=q.next
            p=p.next

        # deal with random
        res=[]
        p=head
        while p!=None:
            if not p.random:
                res.append(-1)
            else:
                res.append(self.searchNodeidx(head,p.random))
            p=p.next

        # build the radom list
        q=copyrdm
        for i in xrange(len(res)):
            if res[i]!=-1:
                q.random=self.searchNode(copyrdm,res[i])
            q=q.next
            
        return copyrdm
        