# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None: 
            return True
        elif root.left is None and root.right is not None:
            if root.right.left is not None or root.right.right is not None:
                return False
        elif root.right is None and root.left is not None:
            if root.left.left is not None or root.left.right is not None:
                return False
        cond = abs(self.calc_depth(root.left) - self.calc_depth(root.right)) < 2
        return cond and self.isBalanced(root.left) and self.isBalanced(root.right) 
    
    def calc_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.calc_depth(root.left), self.calc_depth(root.right))
            
