class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # # Check Rows
        # for i in range(9):
        #     valid_set = set()
        #     for j in range(9):
        #         if board[i][j] != ".":
        #             if board[i][j] in valid_set:
        #                 return False
        #             valid_set.add(board[i][j])
                        
        # # Check Columns
        # for j in range(9):
        #     valid_set = set()
        #     for i in range(9):
        #         if board[i][j] != ".":
        #             if board[i][j] in valid_set:
        #                 return False
        #             valid_set.add(board[i][j]) 

        # # Check sub-box
        # for x in range(0,9,3):
        #     for y in range(0,9,3):
        #         valid_set = set()
        #         for i in range(x, x+3):
        #             for j in range(y, y+3):
        #                 if board[i][j] != ".":
        #                     if board[i][j] in valid_set:
        #                         return False
        #                     valid_set.add(board[i][j])
                                
        # return True

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    
                    if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                        return False
                    
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True