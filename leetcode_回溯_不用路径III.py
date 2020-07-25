class Solution:
    def uniquePathsIII(self, grid):
        ans = [0]
        step = 0
        M, N = len(grid), len(grid[0])

        def dfs(x, y, M, N, step):
            if (x < 0 or x >= M or y < 0 or y >= N or grid[x][y] == -1):
                return
            if (grid[x][y] == 2) and (step==0):
                ans[0] += 1
                return
            grid[x][y] = -1
            dfs(x + 1, y, M, N, step - 1)
            dfs(x - 1, y, M, N, step - 1)
            dfs(x, y + 1, M, N, step - 1)
            dfs(x, y - 1, M, N, step - 1)
            grid[x][y] = 0

        for i in range(M):
            for j in range(N):
                if (grid[i][j] == 1):
                    x, y = i, j
                if (grid[i][j] == 0):
                    step += 1

        dfs(x, y, M, N, step + 1)
        return ans[0]




class Solution:
    def uniquePathsIII(self, grid) -> int:
        cnt = 0
        start_x = start_y = 0
        self.end_x = self.end_y = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt += 1
                elif grid[i][j] == 1:
                    start_x = i
                    start_y = j
                    cnt += 1
                elif grid[i][j] == 2:
                    self.end_x = i
                    self.end_y = j
                    cnt += 1

        self.res = 0
        grid[start_x][start_y] = -1
        self.dfs(grid, m, n, start_x, start_y, cnt, 0)
        return self.res

    def dfs(self, grid, m, n, x, y, cnt, step):
        # 终止条件
        if x == self.end_x and y == self.end_y and step == cnt - 1:
            self.res += 1
            return

        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                tmp = grid[nx][ny]
                grid[nx][ny] = -1
                self.dfs(grid, m, n, nx, ny, cnt, step + 1)
                grid[nx][ny] = tmp
