class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or row == (len(board)-1) or col == 0 or col == (len(board[0]) -1)):
                    self.dfs(board, row, col)
                    
        # print(board)
                    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "D":
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'
                    
    def dfs(self, board, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == 'X':
            return None
        if board[row][col] == 'D':
            return None
        board[row][col] = 'D'
        self.dfs(board, row+1, col)
        self.dfs(board, row-1, col)
        self.dfs(board, row, col+1)
        self.dfs(board, row, col-1)