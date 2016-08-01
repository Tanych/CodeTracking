# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_sum=-1<<31
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
     
        def helper(root):
            """
            the recursive function to find the max when 
            moving down from a root
            """
            if not root: return 0
            # get the max from the left subtree
            # if no max, then start from the curr node
            # the left_max should be 0
            # the left sub-path=>root=> upper. The left sub-path may yield a negative sum
            left_max=max(0,helper(root.left))
            # get the max from the right, same as left
            right_max=max(0,helper(root.right))
            # if the left or right subtree contains the node 
            # make the sum become bigger, than get the sum
            self.max_sum=max(left_max+right_max+root.val,self.max_sum)
            
            # only one branch can choose from the sub tree
            return max(left_max,right_max)+root.val
            
        helper(root)
        return self.max_sum
        
        