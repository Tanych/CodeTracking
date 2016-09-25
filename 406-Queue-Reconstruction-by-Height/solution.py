class Node(object):
    def __init__(self,p):
        self.person=p
        self.hcnt=1
        self.left=None
        self.right=None
        
class Solution(object):
    def reconstructQueue(self,people):
        """
        O(nlgn)---only for taller not fit for taller or equal
        """
        if not people:
            return []
        # sort the people with height descending
        people.sort(cmp=lambda x,y:y[0]-x[0] if x[0]!=y[0] else x[1]-y[1])
        root=Node(people[0])
        for p in people[1:]:
            self.insert(root,p,p[1])
        res=[]
        self.inorder(root,res)
        return res
            
    def insert(self,root,p,hcnt):
        # compare the height cnt with root val
        # if the hight count less than the root
        # go to the left
        if hcnt<root.hcnt:
            if not root.left:
                root.left=Node(p)
            else:
                self.insert(root.left,p,hcnt)
            # increase the root val,means how many number in the left subtree
            root.hcnt+=1
        else:
            if not root.right:
                root.right=Node(p)
            else:
                # decrease the hcnt since it already has root.cnt before
                self.insert(root.right,p,hcnt-root.hcnt)
                
    def inorder(self,root,res):
        """
        inorder traval to get the order
        """
        if not root:
            return 
        self.inorder(root.left,res)
        res.append(root.person)
        self.inorder(root.right,res)
        
    def reconstructQueue_on(self, people):
        """
        O(n^2)
        """
        people=sorted(people,cmp=lambda x,y:y[0]-x[0] if x[0]!=y[0] else x[1]-y[1])
        print people
        res=[]
        for h,i in people:
            res.insert(i,[h,i])
        return res


