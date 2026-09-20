# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.get_diam_depth(root)[1]

    def get_diam_depth(self, root):
        if root is None:
            return (-1,0)
        depth_left, diam_left = self.get_diam_depth(root.left)
        depth_right, diam_right = self.get_diam_depth(root.right)
        if depth_left == -1:
            if depth_right == -1:
                pot_diam = 0
            else:
                pot_diam = depth_right + 1
        else:
            if depth_right == -1:
                pot_diam = depth_left + 1
            else:
                pot_diam = depth_left + depth_right + 2
        
        depth = 1 + max(depth_left, depth_right)
        diameter = max(diam_left, diam_right, pot_diam)
        return depth, diameter

