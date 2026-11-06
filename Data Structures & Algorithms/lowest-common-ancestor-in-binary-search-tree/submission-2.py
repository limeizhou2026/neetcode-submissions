# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #用DFS去分别找到p/q的path 然后以短的length比较两种路径 第一个不同的值出现之前那一个就是 LCA。如果有一条路径是另一段的一部分 那我们用一个 commonP 来不断更新 检查是否相同
        path = []
        path1 = []
        path2 =[]

        if not root or not p or not q:
            return 0

        def dfs(root, target, path):
            if not root:
                return None

            path.append(root)

            if root == target:
                return path

            left_result = dfs(root.left, target, path)
            if left_result:
                return left_result

            right_result = dfs(root.right, target, path)
            if right_result:
                return right_result

            path.pop()
            return None

        dfs(root, p, path1)
        dfs(root, q, path2)

        if not path1 or not path2:
            return None
 
        m = len(path1)
        n =len(path2)

        for i in range(min(m,n)):

            if path1[i] != path2[i]:
                break

            commonP = path1[i]

        return commonP

































        # left nodes values are smaller than right nodes values; vice versa
        # starting from the root, if p/q smaller than root, go to left; vice versa
        #if neither way applies, return the current node which should be at the split of the two nodes
        cur = root

        while cur:
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                # edge cases also included in this senario: one of node is also the ancestor of itself
                #split of two nodes
                return cur