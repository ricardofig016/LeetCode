class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        squares = [[] for i in range(len(board) // 3)]
        for i in range(len(board)):
            row = []
            col = []
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    row += board[i][j]
                if board[j][i] != ".":
                    col += board[j][i]
                if board[i][j] != ".":
                    squares[j // 3] += board[i][j]

            if (i + 1) % 3 == 0:
                for square in squares:
                    if len(set(square)) != len(square):
                        return False
                squares = [[] for i in range(len(board) // 3)]
            if len(set(row)) != len(row):
                return False
            if len(set(col)) != len(col):
                return False

        return True


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
