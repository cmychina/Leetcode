"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。
"""
import collections
class Solution:
    def updateMatrix(self,matrix):
        n = len(matrix)
        m = len(matrix[0])
        #记录结果
        res = [[None for _ in range(m)] for _ in range(n)]
        q = collections.deque()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    q.append([i, j])

        while q:
            x, y = q.popleft()
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and res[nx][ny] == None:
                    res[nx][ny] = res[x][y] + 1
                    q.append([nx, ny])
        return res


    def maxDistance(self, grid):
        n = len(grid)
        m = len(grid[0])
        # res = [[None for _ in range(m)] for _ in range(n)]
        q = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append([i, j])
        steps = -1
        if len(q) == 0 or len(q) == n ** 2:
            return steps
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            # 从陆地向四周扩展，扩展后原地修改为-1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                        q.append((nx, ny))
                        grid[nx][ny] = -1
            steps += 1

        return steps