# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None and subRoot is not None:
            return False
        elif root is not None and subRoot is None:
            return False
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        if left or right:
            return True
        return self.is_same_tree(root, subRoot)
    
    def is_same_tree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        elif root is None and subRoot is not None:
            return False
        elif root is not None and subRoot is None:
            return False
        return root.val == subRoot.val and self.is_same_tree(root.left, subRoot.left) and self.is_same_tree(root.right, subRoot.right)
