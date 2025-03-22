class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y: return

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
        
        for u, v in edges:
            union(u, v)
        
        component_v = {}
        component_e = {}

        for i in range(n):
            root = find(i)
            if root not in component_v:
                component_v[root] = set()
                component_e[root] = 0
            
            component_v[root].add(i)
        
        for u, v in edges:
            root = find(u)
            component_e[root] += 1
        
        complete_count = 0

        for root in component_v:
            num_v = len(component_v[root])
            expected_e = num_v * (num_v - 1) // 2

            if expected_e == component_e[root]:
                complete_count += 1
        
        return complete_count