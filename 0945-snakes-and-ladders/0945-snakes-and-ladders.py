class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        # Helper function to convert the 2D board to 1D list
        def board_to_list(board: List[List[int]]) -> List[int]:
            # Variable to alternate left to right in the row and vice-versa
            parse_left = True
            # Result varibale
            res = []
            
            # Iterate from the last row to first
            for row in range(len(board)-1, -1, -1):
                # If the row has decreasing cells from left to right, add the row to res
                if parse_left:
                    res.extend(board[row])
                    parse_left = False
                # if the row has increasing cells from left to right, reverse the row
                else:
                    res.extend(reversed(board[row]))
                    parse_left = True
            # For any cell that has a ladder to snake decrease the res[i] by 1
            for i in range(len(res)):
                if res[i] != -1:
                    res[i] -= 1
            
            return res
        
        linear = board_to_list(board)
        size = len(linear)
        # BFS approach to find the minimum number of dice rolls to reach the last square
        q = deque()
        q.append((0,0))
        seen = set([0])

        while q:
            (spot, moves) = q.popleft()

            for roll in range(1, 7):
                new_spot = spot + roll

                if new_spot >= size:
                    continue
                
                next_spot = linear[new_spot]
                if next_spot == -1:
                    next_spot = new_spot
                
                if next_spot == size -1:
                    return moves + 1
                
                if next_spot not in seen:
                    seen.add(next_spot)
                    q.append((next_spot, moves+1))
        
        return -1

