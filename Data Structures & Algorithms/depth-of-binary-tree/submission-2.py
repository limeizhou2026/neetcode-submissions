# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        from collections import deque
        q = deque()

        if not root:
            return 0

        def bfs(root, depth):

            if not root:
                return

            q.append((root, depth+1))

            while q:
                current, depth = q.popleft()
                if current.left:
                    q.append((current.left, depth+1))
                if current.right:
                    q.append((current.right, depth+1))

            return depth


        height = bfs(root, 0)
        return height




































        q =deque()
        level = 0
        if not root:
            return 0
        
        if root:
                q.append(root)
        
        while q:
            for i in range(len(q)):
                node= q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level +=1
        
        return level

