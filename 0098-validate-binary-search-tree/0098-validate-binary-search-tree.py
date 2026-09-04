# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):
            
            # Empty tree/subtree is valid
            if not node:
                return True
            
            # Node must be strictly between low and high
            if node.val <= low or node.val >= high:
                return False
            
            # Validate left and right subtrees
            return (
                validate(node.left, low, node.val)
                and
                validate(node.right, node.val, high)
            )
        
        return validate(root, float("-inf"), float("inf"))