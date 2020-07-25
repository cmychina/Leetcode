class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m=len(grid)
        n=len(grid[0])
        ##k表示当前组成的最大面积k
        def dfs(grid,i,j):
            if not 0<=i<m or not 0<=j<n or grid[i][j]==0:
                return 0
            grid[i][j]=0
            k=1
            k+=dfs(grid,i+1,j)
            k+=dfs(grid,i-1,j)
            k+=dfs(grid,i,j+1)
            k+=dfs(grid,i,j-1)
            return k
        maxk=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    k=dfs(grid,i,j)
                    maxk=max(maxk,k)
        return maxk

class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        visited=set()
        def dfs(i,j):
            if  0<=i<m and  0<=j<n and grid[i][j]==1 and (i,j) not in visited:
                #等于1标记为0
                visited.add((i,j))
                k=1
                k+=dfs(i + 1, j)
                k+=dfs(i, j + 1)
                k+=dfs( i - 1, j)
                k+=dfs(i, j - 1)
                #visited.remove((i,j))
                return k
            else:
                return 0


        aera=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    tmp=dfs(i,j)
                    aera=max(tmp,aera)

        return aera

    def MundaneDFS(self,grid):
        if not grid:
            return 0
        M=len(grid)
        N=len(grid[0])
        d=[(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(x,y):
            #表示当前x,y可走
            grid[x][y]=0
            k = 1
            for dx,dy in d:
                nx=x+dx
                ny=y+dy
                if 0<=nx<M and 0<=ny<N and grid[nx][ny]==1:
                    k+=dfs(nx,ny)
            return k

        area=0
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    cur=dfs(i,j)
                    area=max(cur,area)
        return area

    def MundaneBFS(self,grid):
        if not grid:
            return 0
        M = len(grid)
        N = len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x,y):
            queue=[(x,y)]
            cnt=1
            grid[x][y]=0
            while queue:
                x,y=queue.pop()
                for dx,dy in d:
                    nx=x+dx
                    ny=y+dy
                    if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 1:
                        queue.append((nx,ny))
                        grid[nx][ny]=0
                        cnt+=1
            return cnt

        area = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    cur = bfs(i, j)
                    area = max(cur, area)
        return area


if __name__ == "__main__":
    s = Solution()

    grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    #print(s.maxAreaOfIsland(grid))
    print(s.MundaneBFS(grid))

