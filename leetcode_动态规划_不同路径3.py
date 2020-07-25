class Solution:
    def uniquePathsIII(self, grid):

        def dfs(v,left):
            visited[v//C][v%C] = True
            left -= 1
            if left == 0 and v == end:
                visited[v//C][v%C] = False
                return 1
            res = 0
            for i,j in d:
                tmp_x = v//C + i
                tmp_y = v%C + j
                if 0 <= tmp_x < R and 0 <= tmp_y < C and grid[tmp_x][tmp_y] == 0 and not visited[tmp_x][tmp_y]:
                    res += dfs(tmp_x * C + tmp_y,left)
            visited[v//C][v%C] = False
            return res


        R = len(grid)
        C = len(grid[0])
        visited = [[False for _ in range(C)] for _ in range(R)]
        start = 0
        end = 0
        left = R * C
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    start = i * C + j
                    grid[i][j] = 0
                elif grid[i][j] == 2:
                    end = i * C + j
                    grid[i][j] = 0
                elif grid[i][j] == -1:
                    left -= 1
        return dfs(start,left)

if __name__=="__main__":
    s=Solution()
    n=[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    print(s.uniquePathsIII(n))