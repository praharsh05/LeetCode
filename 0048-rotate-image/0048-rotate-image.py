class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        edge_len = len(matrix)

        top = 0
        bottom = edge_len - 1

        while top < bottom:
            for col in range(edge_len):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1
        
        for row in range(edge_len):
            for col in range(row + 1, edge_len):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp