# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #using DFS to traverse the nodes from root, the good nodes should be within the range between root node value to the target node value, including the root node itself
        good = 0
        def dfs(root, maxVal):
            nonlocal good

            if not root:
                return 0

            if root.val >= maxVal:
                good+=1
                maxVal =max(maxVal, root.val)

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)



        dfs(root, root.val)
        return good