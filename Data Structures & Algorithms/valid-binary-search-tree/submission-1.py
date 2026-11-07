# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #a valid BST is a tree where its left subtrees < the root while the right subtrees > the root
        def valid(node, left, right):
            #if the node is Null, it's a valid BST
            if not node:
                return True
            #if it does not satisfy teh below relation; return False
            if not left < node.val < right:
                return False
            #check the left child and right child with the updated left and right bounds
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        # when start from the root, set the left and right bounds as infinite separately
        return valid(root, float("-inf"), float("inf"))