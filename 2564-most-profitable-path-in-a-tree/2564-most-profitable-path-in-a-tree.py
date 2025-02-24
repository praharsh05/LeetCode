class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        tree = defaultdict(list)

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        parent = [-1] * n
        q = deque([0])
        parent[0] = 0

        while q:
            u = q.popleft()
            for v in tree[u]:
                if v == parent[u]: continue

                parent[v] = u
                q.append(v)
        
        bobTime = [float('inf')] * n
        t= 0
        cur = bob
        while True:
            bobTime[cur] = t
            if cur == 0: break
            cur = parent[cur]
            t += 1
        
        res = float('-inf')

        def dfs(u, t, currProfit, par):
            nonlocal res
            if t < bobTime[u]:
                currProfit += amount[u]
            elif t == bobTime[u]:
                currProfit += amount[u]//2
            
            isLeaf = True

            for v in tree[u]:
                if v == par: continue
                isLeaf = False
                dfs(v, t+1, currProfit, u)
            
            if isLeaf:
                res = max(res, currProfit)

        dfs(0,0,0,-1)
        return res