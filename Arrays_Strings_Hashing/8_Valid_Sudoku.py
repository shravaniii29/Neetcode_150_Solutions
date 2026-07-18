# Time Complexity: O(1)
# - The board is always 9x9 (81 cells), so we always perform
#   at most 81 iterations.
# - In general, for an n×n Sudoku board, it would be O(n²).

# Space Complexity: O(1)
# - We use hash sets for 9 rows, 9 columns, and 9 boxes.
# - Since the board size is fixed (9x9), the extra space is constant.

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                num = board[r][c]

                box = (r // 3, c // 3)

                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[box]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

        return True

