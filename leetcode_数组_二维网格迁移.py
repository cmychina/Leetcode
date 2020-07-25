class Solution:
    def shiftGrid(self, grid, k: int):
        line = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                line.append(grid[i][j])
        idx = k % len(line)
        line[:] = line[len(line) - idx:] + line[:len(line) - idx]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = line.pop(0)
        return grid

    #找到首字符，然后依次填补

    def Mundane(self,grid,k):
        n, m = len(grid), len(grid[0])
        sx, sy = (k // m) % n, k % m
        g = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                g[sx][sy] = grid[i][j]
                sy += 1
                if sy == m:
                    sy = 0
                    sx += 1
                    if sx == n:
                        sx = 0
        return g
