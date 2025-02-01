class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        # DFS to search the relation to a query in the graph
        def dfs(graph, start, target):
            
            # If start or target not in the graph then return -1 as there is no relationship
            if start not in graph or target not in graph:
                return -1
            
            # Create a stack and add the start (A[i]) and set the ans as 1 as A[i]/A[i] = 1
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
                        # Example: A/C = A/B * B/C
                        stack.append((neighbor, ans*div))
            
            return -1
        
        # Create a Graph
        dic = defaultdict(list)
        for i in range(len(equations)):
            dic[equations[i][0]].append((equations[i][1], values[i]))
            dic[equations[i][1]].append((equations[i][0], 1/values[i]))
        ans = []

        for x, y in queries:
            ans.append(dfs(dic, x, y))
        
        return ans