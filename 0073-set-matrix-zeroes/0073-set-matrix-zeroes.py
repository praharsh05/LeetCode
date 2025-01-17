class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Variables for row and col
        rows = len(matrix)
        cols = len(matrix[0])

        # Flags for first row and col containing 0
        first_row_0 = False
        first_col_0 = False

        # Check 0 in first row
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_0 = True
                break
        
        # Check 0 in first col
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_0 = True
                break
        
        # Use first row and col as a note
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0], matrix[0][c] = 0, 0
        
        # Set the marked rows to 0
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0
        
        # Set the marked cols to 0
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
        
        # Set the first row to 0 if flag is true
        if first_row_0:
            for c in range(cols):
                matrix[0][c] = 0
        
        # Set the first col to 0 if flag is true
        if first_col_0:
            for r in range(rows):
                matrix[r][0] = 0


        