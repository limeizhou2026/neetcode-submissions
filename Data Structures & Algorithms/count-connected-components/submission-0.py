class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #if the edges are connected, the nodes of the connected edges would eventually use the same root; in this case, we can add all the root nodes into a set; then compute the length of the set which is the number of the connected components 
        #initalize the root node and rank size for each node
        par = [i for i in range(n)]
        rank = [1] * n
        count = 0

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return
            
            if rank[p1] >=rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                return p1

            elif rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
                return p2

        for n1, n2 in edges:
            union_root = union(n1, n2)

        for root in range(n):
            if par[root] == root:
                count+= 1

        return count


            