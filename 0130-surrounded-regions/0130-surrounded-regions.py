class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

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
