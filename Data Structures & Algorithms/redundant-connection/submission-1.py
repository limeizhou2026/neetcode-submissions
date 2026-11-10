class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #每读一条新边，先找两端的 root。root 不同，合并两组；root 相同，说明这条新边会形成环
        #这道题比较特殊 node数量和edge数量一致
        #通常的graph特征是：N 个节点，对应 N - 1 条边
        n = len(edges)
        #the root of each node; 0 never use
        #initialize: the root of each node is themselves
        par = [i for i in range(n+1)] #长度应该n+1 因为0不用
        #is the size of this group/set; 
        #initalize: each node is a separate group which contains only 1 node
        rank = [1] * (n+1) #长度应该n+1 因为还要算0

        #思路：把每一条边的两个node 带进去看看他们的父节点是不是同一个 是的话就证明有环 可以移除 不是的话就合并两个点的父节点

        def find(n):
            #find(n) 是沿着 par 一层层往上走，找到节点 n 所在组的代表。代表的特征是：它的父节点是它自己。
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            #union(n1, n2) 先判断两个节点是不是已经同组。如果是两个不同的组，再决定谁当合并后的代表。
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                return True

            else:
                par[p1] = p2
                rank[p2] += rank[p1]
                return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]































        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # 已经同组，新边会形成环
            if p1 == p2:
                return False
            
            # 小组的代表指向大组的代表
            if rank[p1]> rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            elif rank[p1] < rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]

            else:
                # 一样大时，任选一方当代表
                par[p2] = p1
                rank[p1] += rank[p2]
            return True
        # 按输入顺序处理每条边
        for n1, n2 in edges:
            #KEY：call function 要把arguments带上
            ## 调用 union，判断是否形成环
            if not union(n1, n2):
                return [n1, n2]
