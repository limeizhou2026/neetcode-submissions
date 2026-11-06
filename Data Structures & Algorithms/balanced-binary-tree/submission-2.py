# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #用DFS分别traverse左边和右边路径 然后比较两边的height差是否大于1
        if not root:
            return True

        def dfs(root):
            if not root:
                return 0

            left_h = dfs(root.left)
            right_h = dfs(root.right)

            if left_h == -1 or right_h == -1:
                    return -1

            if abs(left_h - right_h) >1:
                return -1

            return max(left_h, right_h) +1

        return dfs(root) != -1            


































        #using DFS to check the height of the deepest node of each side is balanced which means if their abs is less than 1 or not; this can be applied to L/R side as weell
        def dfs(root):
            if not root:
                # !!! DO add "0" to teh return below otherwise the following computation for the abs would not WORK
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

        #!!! it should return the boolean when the return amount NOT equal to -1
        return dfs(root) != -1