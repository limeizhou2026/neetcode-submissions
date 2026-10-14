class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c):
           
            if r<0 or r>= rows or c < 0 or c>= cols:
                return
            if board[r][c] != "O":
                return
           
            board[r][c] = "S"

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X":
                    continue
                if i == 0 or j == 0 or i== rows-1 or j == cols-1:
                    dfs(i, j)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    continue

                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
