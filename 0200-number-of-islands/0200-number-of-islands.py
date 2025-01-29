class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # variable to keep track of the islands found
        islands = 0
        # Variable to track of the visited cells
        visited = set()
        # Variables to store the dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # BFS function to explore all the cells
        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                # Possible directions for cell to be connected to an island
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                # Explore neighbours
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    # Check if the new cell is within bounds, is an island and has not 
                    # been visited
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
        
        # Process each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands +=1
                    bfs(r, c)
        
        return islands
