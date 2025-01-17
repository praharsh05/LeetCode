class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        edge_len = len(matrix)
        # Transpose the matrix
        for row in range(edge_len):
            for col in range(row + 1, edge_len):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        # Reverse each row
        for row in range(edge_len):
            matrix[row].reverse()