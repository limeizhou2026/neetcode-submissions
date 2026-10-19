# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        root_array = []
        res = 0
        def dfs(root):
            if not root:
                return 0

            root_array.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        print(root_array)
        root_array.sort()
        return root_array[k-1]

