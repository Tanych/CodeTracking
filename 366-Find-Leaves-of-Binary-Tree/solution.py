# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lmapping=[]
    
    def helper(self,root):
        if not root: return -1
        left=self.helper(root.left)
        right=self.helper(root.right)
        height=max(left,right)+1
        if height<len(self.lmapping):
            self.lmapping[height].append(root.val)
        else:
            self.lmapping.append([root.val])
            
        return height
        
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        self.helper(root)
        return self.lmapping
        