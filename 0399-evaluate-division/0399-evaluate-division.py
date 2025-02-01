class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        dic = defaultdict(list)
        for i in range(len(equations)):
            dic[equations[i][0]].append((equations[i][1], values[i]))
            dic[equations[i][1]].append((equations[i][0], 1/values[i]))
        
        # DFS to search the relation to a query
        def dfs(graph, start, target):

            if start not in graph or target not in graph:
                return -1
            
            stack = []
            stack.append((start, 1))
            visited = set()

            while stack:
                node, ans = stack.pop()
                visited.add(node)

                if node == target:
                    return ans
                
                for neighbor, div in graph[node]:
                    if neighbor not in visited:
                        stack.append((neighbor, ans*div))
            
            return -1
        
        ans = []

        for x, y in queries:
            ans.append(dfs(dic, x, y))
        
        return ans