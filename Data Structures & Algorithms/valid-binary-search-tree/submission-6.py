# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))

    def dfs(self, node, lowest, highest):
        if node is None:
            return True
        
        if not(node.val < highest and node.val > lowest):
            return False
        
        return self.dfs(node.left, lowest, node.val) and self.dfs(node.right, node.val, highest)

        







    def dfs_left(self, node, highest):
        if node is None:
            return True
        
        if node.val >= highest:
            return False
        else:
            if node.right is not None and node.right.val > node.val and node.right.val < highest:
                self.dfs_right(node.right, node.val)
        
        return self.dfs_left(node.left, node.val)

    def dfs_right(self, node, lowest):
        if node is None:
            return True
        
        if node.val <= lowest:
            return False
        else:
            if node.left is not None and node.left.val < node.val and node.left.val > lowest:
                self.dfs_left(node.left, node.val) 
        
        return self.dfs_right(node.right, node.val)
