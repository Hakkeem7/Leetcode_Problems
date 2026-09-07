# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # Node not found
        if root is None:
            return None

        # Search left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Search right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Found the node
        else:

            # Case 1: No left child
            if root.left is None:
                return root.right

            # Case 2: No right child
            if root.right is None:
                return root.left

            # Case 3: Two children
            # Find smallest node in right subtree
            successor = root.right

            while successor.left:
                successor = successor.left

            # Copy successor value
            root.val = successor.val

            # Delete successor
            root.right = self.deleteNode(root.right, successor.val)

        return root