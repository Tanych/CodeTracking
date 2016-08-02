# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.f_node=None
        self.s_node=None
        self.f_succ_node=None
        # if set none, can't compare at first
        self.pre_node=TreeNode(-(1<<31))
        
    def rechelper(self,root):
        if not root:
            return
        # left
        self.rechelper(root.left)
        
        # mid
        # if find the first root.val larger than previous node
        # mark the first node,it would be the sitution with 5,2
        if root.val<=self.pre_node.val:
            if not self.f_node:
                self.f_node=self.pre_node
                self.f_succ_node=root
            else:
                # if move two node and it's normal bst then move on
                if self.pre_node.val>=self.f_succ_node.val:
                    self.s_node=root
                # else found the second node
                else:
                    self.s_node=self.pre_node
                    
        self.pre_node=root
        # right
        self.rechelper(root.right)
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # Only morris can implement the traversal in constant space
        # stack and recusive not the way
        
        # if we using recusive
        
        # for example 5,2,3,4,1
        self.rechelper(root)
        # swap
        #print self.f_node.val,self.s_node.val
        if self.s_node:
            self.f_node.val,self.s_node.val= self.s_node.val,self.f_node.val
        else:
            self.f_node.val,self.f_succ_node.val= self.f_succ_node.val,self.f_node.val
        
        