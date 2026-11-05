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
