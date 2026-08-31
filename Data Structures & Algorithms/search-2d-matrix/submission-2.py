class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            m = (l + r) // 2
            row, col = m // COLS, m % COLS
            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True

        return False