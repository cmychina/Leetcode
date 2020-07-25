# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        M = len(matrix)
        N = len(matrix[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.visited = set()

        def dfs(x, y, k):
            if not (0 <= x < M and 0 <= y < N and matrix[x][y] == path[k] and (x, y) not in self.visited):
                return False
            if matrix[x][y] == path[k] and k == len(path) - 1:
                return True
            self.visited.add((x, y))
            k = dfs(x + 1, y, k + 1) or dfs(x - 1, y, k + 1) or dfs(x, y + 1, k + 1) or dfs(x, y - 1, k + 1)
            self.visited.remove((x, y))
            return k

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == path[0]:
                    res = dfs(i, j, 0)
                    if res == True:
                        return True

        return False
