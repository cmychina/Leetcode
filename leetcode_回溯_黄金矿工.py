class Solution:
    def getMaximumGold(self, grid):
        m,n=len(grid),len(grid[0])
        def dfs(x,y):
            ans=0
            path=set()
            tmp=grid[x][y]
            grid[x][y]=0
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=i<m and 0<=j<n and grid[i][j]>0:
                    cur,p=dfs(i,j)
                    if cur>ans:
                        ans=cur
                        path=p
            grid[x][y]=tmp
            path.add((x,y))
            return ans+tmp,path

        sean=set()
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0 and (i,j) not in sean:
                    cur,path=dfs(i,j)
                    if cur>ans:
                        ans=cur
                        sean=path
        return ans


    def Mundane(self,grid):

        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        n = len(grid)
        m = len(grid[0])

        self.profit = 0

        def dfs(x, y, cur, visited):
            cur += grid[x][y]
            self.profit = max(cur, self.profit)
            for dx, dy in direction:
                x_n = x + dx
                y_n = y + dy
                if 0 <= x_n < n and 0 <= y_n < m and grid[x_n][y_n] > 0 and (x_n, y_n) not in visited:
                    visited.append((x_n, y_n))
                    dfs(x_n, y_n, cur, visited)
                    visited.pop()

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    dfs(i, j, 0, [(i, j)])

        return self.profit

    def getMaximumGold(self, grid):
        self.profit = 0
        L1 = len(grid)
        L2 = len(grid[0])

        def backtrack(i, j, cur):
            if i < 0 or j < 0 or i > L1 - 1 or j > L2 - 1 or grid[i][j] == 0:
                if cur >= self.profit:
                    self.profit = cur
                return

            tmp = grid[i][j]
            grid[i][j] = 0
            backtrack(i + 1, j, cur + tmp)
            backtrack(i - 1, j, cur + tmp)
            backtrack(i, j + 1, cur + tmp)
            backtrack(i, j - 1, cur + tmp)
            grid[i][j] = tmp

        for i in range(L1):
            for j in range(L2):
                backtrack(i, j, 0)
        return self.profit