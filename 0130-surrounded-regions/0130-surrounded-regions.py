class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # def dfs(row, col, curr, board):
        #     # mark the current cell as visited
        #     curr[row][col] = True
        #     n, m = len(board), len(board[0])

        #     # Directions for traversing
        #     directions = [[1,0], [-1,0], [0,1], [0,-1]]

        #     for dr, dc in directions:
        #         nrow, ncol = row + dr, col + dc
        #         # Check bounds, visitation, and if its a O
        #         if 0 <= nrow < n and 0 <= ncol < m and not curr[nrow][ncol] and board[nrow][ncol] == "O":
        #             dfs(nrow, ncol, curr, board)
        
        # n, m = len(board), len(board[0])
        # # Visited matrix to track process cells
        # vis = [[False] * m for _ in range(n)]

        # # Traverse border rows
        # for i in range(n):
        #     if not vis[i][0] and board[i][0] == "O":
        #         dfs(i, 0, vis, board)
        #     if not vis[i][m-1] and board[i][m-1] == "O":
        #         dfs(i, m-1, vis, board)
        
        # # Traverse border cols
        # for j in range(m):
        #     if not vis[0][j] and board[0][j] == "O":
        #         dfs(0, j, vis, board)
        #     if not vis[n-1][j] and board[n-1][j] == "O":
        #         dfs(n-1, j, vis, board)

        # # Flip unvisted "O" to "X", retain visited "O" as it is
        # for i in range(n):
        #     for j in range(m):
        #         if not vis[i][j] and board[i][j] == "O":
        #             board[i][j] = "X"

        def dfs(row, col):
            """Mark 'O' connected to borders with '#'"""
            board[row][col] = "#"
            n, m = len(board), len(board[0])

            # Directions for traversal
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                nrow, ncol = row + dr, col + dc
                # Check bounds and if it's an 'O'
                if 0 <= nrow < n and 0 <= ncol < m and board[nrow][ncol] == "O":
                    dfs(nrow, ncol)

        n, m = len(board), len(board[0])

        # Mark all 'O's connected to borders using DFS
        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][m - 1] == "O":
                dfs(i, m - 1)

        for j in range(m):
            if board[0][j] == "O":
                dfs(0, j)
            if board[n - 1][j] == "O":
                dfs(n - 1, j)

        # Convert all remaining 'O' → 'X', and '#' → 'O'
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
