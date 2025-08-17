# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ismirrored(root_left: Optional[TreeNode], root_right: Optional[TreeNode]) -> bool:
            if not root_left and not root_right:
                return True
            if not root_left or not root_right:
                return False
            
            return (root_left.val == root_right.val and
                   ismirrored(root_left.left,root_right.right) and
                   ismirrored(root_left.right,root_right.left))
        
        if not root:
            return True
        
        return ismirrored(root.left,root.right)