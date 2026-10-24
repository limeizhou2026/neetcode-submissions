# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #using dfs-preorder to traverse the path for each side
        good = 0

        def dfs_preorder(root, maxval):
            nonlocal good
            if not root:
                return
            
            if root.val >= maxval:
                maxval = max(maxval, root.val)

            dfs_preorder(root.left, maxval)
            dfs_preorder(root.right, maxval)
        
        dfs_preorder(root, float("-inf"))



























        #using DFS to traverse the nodes from root, also we keep recording maxVal along the path. The good nodes should be bigger than or equal to the max value, including the root node itself
        good = 0
        def dfs(root, maxVal):
            nonlocal good
            #in this case, it won't count the Null node
            if not root:
                return 0

            #we only count when the current root value is bigger or equal to the maxVal and only update the maxVal at this senario
            if root.val >= maxVal:
                good+=1
                maxVal =max(maxVal, root.val)

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        #initialize the function with the root node and the root.val should be the initialized maxVal
        dfs(root, root.val)
        return good