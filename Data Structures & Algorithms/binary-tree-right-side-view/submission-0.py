# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        # if root.right is not None:
        #     return [root.val, root.right.val]
        # if root.left is not None:
        #     return [root.val, root.left.val]
        
        left_list = self.rightSideView(root.left)
        right_list = self.rightSideView(root.right)
        return [root.val] + right_list + left_list[len(right_list)::]