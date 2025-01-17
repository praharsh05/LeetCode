class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Variables to keep track of directions we are moving
        x = 0 #Rows
        y = 0 #Column
        dir_x = 1 #Jump in x
        dir_y = 0 #Jump in y
        res = [] # Result list

        # Iterate over the whole matrix
        for _ in range(len(matrix) * len(matrix[0])):
            # Add the visiting node to the result and change the node to -101 which is outside the constraints
            res.append(matrix[y][x])
            matrix[y][x] = -101
            # Check if we reach the end of a row or column or or the node is -101
            if not 0 <= x + dir_x < len(matrix[0]) \
                or not 0 <= y + dir_y < len(matrix) \
                or matrix[y+dir_y][x+dir_x] == -101:
                # change the jump vairables to follow the spiral
                dir_x, dir_y = -dir_y, dir_x
            
            # increment x and y 
            x += dir_x
            y += dir_y
        
        return res
