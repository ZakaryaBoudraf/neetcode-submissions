class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
        # Check cols
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
        # Check 3x3 boxes
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_r + i][box_c + j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)
        return True