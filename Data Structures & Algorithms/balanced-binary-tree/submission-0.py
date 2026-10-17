# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #using DFS to check the height of the deepest node of each side is balanced which means if their abs is less than 1 or not; this can be applied to L/R side as weell
        def dfs(root):
            if not root:
                return 0

            #check the L side of the tree
            left_side = dfs(root.left)
            #check teh right side
            right_side = dfs(root.right)
            #check either side is balanced or not
            if left_side == -1 or right_side ==-1:
                return -1

            #check if the main both sides are balanced or not 
            if abs(left_side - right_side) > 1:
                return -1
            
            #if balanced we would return the depth of the height of this level of nodes
            #since the height does not count the current level so we should add 1 to count current level
            return max(left_side, right_side) +1

        return dfs(root) != -1