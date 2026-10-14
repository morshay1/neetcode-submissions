# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if root is None:
            return output
        if root.left is None and root.right is None:
            output.append([root.val])
            return output

        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)

        if len(left) > len(right):
            for i in range(len(right)):
                output.append(left[i] + right[i])
            output += (left[len(right)::])
        else:
            for i in range(len(left)):
                output.append(left[i] + right[i])
            output += (right[len(left)::])

        output.insert(0, [root.val])

        return output
           
        
