class Solution:
    def solve(self, board):
        m=len(board)
        n=len(board[0])

        def dfs(i,j):
            if not 0<i<m or not 0<j<n or board[i][j] !="O":
                return
            #标记O
            board[i][j]="#"
            dfs(i, j-1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        #与边界联通的所有O都标记为#
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
        return board
    




if __name__ == "__main__":
    s = Solution()
    board=[["X","X","X","X"],["X","O","O","X"],
           ["X","X","O", "X"],["X","O","X","X"]]
    print(s.solve(board))
