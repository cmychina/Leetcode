class Solution:
    def closedIsland(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        M = len(grid)
        N = len(grid[0])

        def dfs(i,j):
            grid[i][j] = 1
            for x,y in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = i+x, j+y
                #深搜停止的边界条件为grid[i][j]==1
                if 0<=nx<M and 0<=ny<N and grid[nx][ny]==0:
                    dfs(nx,ny)
            return

        #先把边界0填充为1
        for i in range(M):
            if grid[i][0]==0:
                dfs(i,0)
            if grid[i][N-1]==0:
                dfs(i,N-1)
        for j in range(N):
            if grid[0][j]==0:
                dfs(0,j)
            if grid[M-1][j]==0:
                dfs(M-1,j)

        count = 0
        #下面开始处理内部0
        for i in range(1,M-1):
            for j in range(1,N-1):
                if grid[i][j]==0:
                    count += 1
                    dfs(i,j)
        return count
