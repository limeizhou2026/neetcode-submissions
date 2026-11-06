# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #找最长深度用DFS 有“最”就应该用max 左右两边的深度之和 有时候可能不经过root child自己下面的左右两边children深度加起来就是最长
        #要分清depth：从整棵树的根走到当前节点，有多深。
        #height：从当前节点往下走，最长能走多少层。
        res = 0
        if not root:
            return 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            #KEY：不用再加“if left_h” 因为上一步已经确认了dfs（None）会返回0
            #如果加if 在left/right是None的时候 left_h/right_h就不会赋值
            #就会报错
            left_h = dfs(root.left)
            right_h = dfs(root.right)

            res = max(res, left_h + right_h)
            return max(left_h, right_h)+1

        dfs(root)
        return res

































        
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
