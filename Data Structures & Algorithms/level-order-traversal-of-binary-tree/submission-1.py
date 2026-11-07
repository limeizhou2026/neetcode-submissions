# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #卡点：只想到了用q然后level相同的一层要放在一个【】里面 但没想到可以用一个空level【】 在每一层rest 然后append每一层的node进result

        from collections import deque
        res = []

        if not root:
            return []

        q = deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                current = q.popleft()
                if current:
                    level.append(current.val)
                    q.append(current.left)
                    q.append(current.right)
            
            if level:
                res.append(level)

        return res


































        #using BFS to travel each level of node; when pop up a node from the left, append its children to the q.
        q = deque()
        res = []
        # initialize the q with the root
        q.append(root)
        while q:
            # set a level list to append the nodes of each level then append to result, this will result in a [[]] result
            level = []
            #!!! this step is critical!!! it sets the system to deal with the nodes at each level every time, in this case, level would include all node at the specific level
            for i in range(len(q)):
                node = q.popleft()
                # if node is Null, skip it
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # when the nodes are Null, level will be empty list. In this case, res should not append 
            if level:
                        res.append(level)

        return res

