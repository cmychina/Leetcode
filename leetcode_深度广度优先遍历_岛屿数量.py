class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        visited=set()
        def dfs(i,j):
            if  0<=i<m and  0<=j<n and grid[i][j]=='1' and (i,j) not in visited:
                #等于1标记为0
                visited.add((i,j))
                dfs( i + 1, j)
                dfs(i, j + 1)
                dfs( i - 1, j)
                dfs(i, j - 1)


        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1'and (i,j) not in visited:
                    dfs(i,j)
                    count+=1
        return count

if __name__ == "__main__":
    # import sys
    # seq = []
    # res=[]
    # while 1:
    #     line = sys.stdin.readline().strip()
    #     if line == '':
    #         break
    #     seq.append(line.split())
    #
    # print(seq)
    grid=[["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    s=Solution()
    print(s.numIslands(grid))