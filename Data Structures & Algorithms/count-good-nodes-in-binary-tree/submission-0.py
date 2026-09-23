# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.dfs(root, root.val)

    def dfs(self, node, highest_so_far):
        output = 0
        
        if node is None:
            return output
        
        if node.val >= highest_so_far:
            output += 1
            highest_so_far = node.val

        return output + self.dfs(node.left, highest_so_far) + self.dfs(node.right, highest_so_far)
