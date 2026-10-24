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
            #应当重点关注当前节点是否valid， 确定以后才能让maxval更新value。不应该用root的左右孩子和max比；左右孩子会在自己的recursion部分得出答案
            if root.val >= maxval:
                good+=1
                maxval = max(maxval, root.val)

            dfs_preorder(root.left, maxval)
            dfs_preorder(root.right, maxval)
        
        dfs_preorder(root, float("-inf"))
        return good



























    