# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #dfs to explore, explore right side first to save the right nodes from right side into a res; meanwhile count the levels of both side, if the level of left side is bigger than right side, then also include the right children of left side
        res = []
        def dfs(root, depth):
            if not root:
                return 

            # if depth == len(res) proving that this level has not been visited yet, thus we can append the first node we encouter to the res
            if depth == len(res):
                res.append(root.val)

            #traverse the right subtree first, in this case, all the qualified nodes from right side are appended into res 
            dfs(root.right, depth+1)

            #trverse left side afterwards; then we will only need to append the nodes that at the bigger depth
            dfs(root.left, depth+1)

            #call the function with arguments and initialize depth as 0
        dfs(root, 0)
        return res

            


            