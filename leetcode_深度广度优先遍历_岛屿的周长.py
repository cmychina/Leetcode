#上下左右几个0边长就加几
class Solution:
    def islandPerimeter(self, grid):
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        visited=set()
        def dfs(i,j,s):
            if s>1:
                return 0
            # 边界或者取值为0，则返回1
            if  not 0<=i<m or not  0<=j<n or grid[i][j]==0:
                return 1
            k = 0
            k+=dfs(i + 1, j,s+1)
            k+=dfs(i, j + 1,s+1)
            k+=dfs(i - 1, j,s+1)
            k+=dfs(i, j - 1,s+1)
            return k
        aera = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tmp = dfs(i, j,0)
                    aera+=tmp

        return aera
if __name__ == "__main__":
    s = Solution()

    grid=[[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
    print(s.islandPerimeter(grid))