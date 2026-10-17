# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #check if root of both tree is null
        #both null = true
        #either null = false or if none is null, q.val != p.val: return false

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p and q and p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))