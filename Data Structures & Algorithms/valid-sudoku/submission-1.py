class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                digit = int(board[r][c])
                bit = 1 << (digit - 1)
                if bit & rows[r]:
                    return False
                if bit & cols[c]:
                    return False
                if bit & squares[(r // 3) * 3 + (c // 3)]:
                    return False

                rows[r] |= bit
                cols[c] |= bit
                squares[(r // 3) * 3 + (c // 3)] |= bit

        return True