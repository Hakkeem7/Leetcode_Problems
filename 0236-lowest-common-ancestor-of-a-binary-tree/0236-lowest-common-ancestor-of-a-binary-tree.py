# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        # If tree is empty
        if root is None:
            return None

        # If we found p or q
        if root == p or root == q:
            return root

        # Search in left side
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search in right side
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q found on different sides
        if left is not None and right is not None:
            return root

        # Return whichever side found a node
        if left is not None:
            return left

        return right


