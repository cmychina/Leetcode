class Solution:
    def exist(self,board, word):
        m = len(board)
        n = len(board[0])

        self.visited=set()
        self.path=[]

        def dfs(i, j, k):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k] or (i, j) in self.visited:
                return False

            if board[i][j] == word[k] and k == len(word) - 1:
                self.path.append((i, j))
                return True

            self.visited.add((i,j))
            self.path.append((i, j))

            return dfs(i + 1, j, k + 1) or \
                   dfs(i - 1, j, k + 1) or \
                   dfs(i, j + 1, k + 1) or \
                   dfs(i, j - 1, k + 1)


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j,0):
                        print(self.path)
                        return True


class Solution:
    def exist(self, board, word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def helper(i, j, k, visited):

            if k == len(word):
                return True

            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited and board[tmp_i][tmp_j] == word[k]:
                    visited.add((tmp_i, tmp_j))
                    if helper(tmp_i, tmp_j, k + 1, visited):
                        return True
                    visited.remove((tmp_i, tmp_j))  # 回溯
            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and helper(i, j, 1, {(i, j)}):
                    return True
        return False

class Solution:
    def exist(self, board, word: str) -> bool:
        self.m,self.n=len(board),len(board[0])

        def dfs(i,j,s):
            if not s:
                return True
            if not (0<=i<self.m and 0 <=j<self.n and board[i][j]==s[0]):
                return False
            tmp=board[i][j]
            board[i][j]=''
            res=dfs(i-1,j,s[1:]) or dfs(i+1,j,s[1:]) or dfs(i,j-1,s[1:]) or dfs(i,j+1,s[1:])
            board[i][j]=tmp
            return res

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j]==word[0]:
                    if dfs(i,j,word):
                        return True
        return False



if __name__=="__main__":
    s=Solution()
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word='ABFCEE'
    print(s.exist(board,word))
