# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # using DFS to explore the nodes at each side
        # when explore each level, add 1 to the depth
        # add the max depth of each side = diameter of this tree
        res = 0
        def dfs(root):
            if not root:
                return 0
            
            left_side = dfs(root.left)
            right_side = dfs(root.right)
            nonlocal res
            res = max(res, left_side + right_side)
            #return height to the parent/upper level
            return max(left_side, right_side) + 1
        
        dfs(root)
        return res            
