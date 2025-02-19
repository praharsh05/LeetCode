class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        count = {}
        for i in range(len(edges)):
            for j in range(len(edges[0])):
                count[edges[i][j]] = count.get(edges[i][j], 0) + 1
        
        for key in count:
            if count[key] == n: return key
        