class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #using DFS；从edge出发，在edge上的O以及和它connect的O保持不变
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c):
            if r<0 or r>=rows or c<0 or c>=cols:
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
                
                if i == 0 or i == rows-1 or j==0 or j==cols-1:
                    dfs(i, j)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    continue
                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "S":
                    board[r][c] = "O"




        rows = len(board)
        cols = len(board[0])
        def dfs(r, c):
           
            if r<0 or r>= rows or c < 0 or c>= cols:
                return
            #make sure no matter encounter S or X, it would return
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
                    #only visit the cells that on the edge, do remember to include teh last row and column as the edge as well
                if i == 0 or j == 0 or i== rows-1 or j == cols-1:
                    dfs(i, j)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    continue
                #since the DFS only go through the cells connected with edge, the qualified region would stay as is.
                #Do remember to change the original O to X first before changing S to O; otherwise the Os changed from S would be modified to X when do the below order reversed
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"































      