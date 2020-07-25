"""
思路1：dfs
思路2：并查集
"""
class Solution:
    def numIslands(self, grid) -> int:
        """
        找所有连通的1
        """
        if not grid:
            return 0
        M=len(grid)
        N=len(grid[0])
        def dfs(i,j):
            if not (0<=i<M and 0<=j<N and grid[i][j]=='1'):
                return
            grid[i][j]='0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        cnt=0
        for i in range(M):
            for j in range(N):
                if grid[i][j]=='1':
                    dfs(i,j)
                    cnt+=1
        return cnt

#并查集的一个简单实现
class Solution:
    def numIslands(self, grid) -> int:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    for x, y in [[-1, 0], [0, -1]]:
                        nx = i + x
                        ny = j + y
                        if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == "1":
                            union(nx * row + ny, i * row + j)

        res = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    res.add(find((i * row + j)))

        return len(res)

#完整并查集实现 1.路径压缩，2.按秩合并
class UnionFind:

    def __init__(self, grid):
        M, N = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (M * N)
        self.rank = [0] * (M * N)#按秩合并
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    self.parent[i * N + j] = i * N + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            #低秩合并给高秩
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def numIslands(self, grid) -> int:
        M = len(grid)
        if M == 0:
            return 0
        N = len(grid[0])
        uf = UnionFind(grid)
        for x in range(M):
            for y in range(N):
                if grid[x][y] == "1":
                    grid[x][y] = "0"
                    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == "1":
                            uf.union(x * N + y, nx * N + ny)

        return uf.getCount()
