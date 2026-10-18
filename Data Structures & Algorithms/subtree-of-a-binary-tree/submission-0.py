# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #edge cases:
        if not subRoot:
            return True
        # subRoot here must be not Null, otherwise it returned "True" above
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))
    
    # create a helper function to recognize this the subRoot and the root are the same tree
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left)) and (self.sameTree(root.right, subRoot.right))
        