class Solution:
    def solveSudoku(self, board):

        def check(x, y, s):
            for i in range(9):
                #检查(x,y)所在行和列是否出现过s
                if board[i][y] == s or board[x][i] == s:
                    return False
            #检查再一个9宫格内是否存在s
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    if board[x // 3 * 3 + i][y // 3 * 3 + j] == s:
                        return False
            return True

        def backtrack(cur):
            if cur == 81:
                return True
            x, y = cur // 9, cur % 9
            #已有数字
            if board[x][y] != '.':
                return backtrack(cur + 1)

            for i in range(1, 10):
                s = str(i)
                if check(x, y, s):
                    board[x][y] = s
                    if backtrack(cur + 1):
                        return True
                    #回溯
                    board[x][y] = '.'
            return False

        backtrack(0)
#O((9!)^9)