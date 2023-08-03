class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = []
        col = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    row += board[i][j]
                    col += board[j][i]
            if len(set(row)) != len(row):
                return False
            if len(set(col)) != len(col):
                return False
            print(f"row: {row}\ncol: {col}")


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

sol = Solution()
print(sol.isValidSudoku(board))
