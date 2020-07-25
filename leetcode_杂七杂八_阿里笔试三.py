class Solution:

    def minPath(self,matrix):
        n=len(matrix)
        m=len(matrix[0])
        self.fly = 5
        self.min_path=float("inf")
        visited=set()
        def dfs(i,j,path):
            if i<0 or i>=n or j<0 or j>=n or matrix[i][j]=="#" or (i,j)  in visited:#跨界和障碍
                return
            if matrix[i][j]=="E":
                self.min_path=min(self.min_path,path)
            visited.add((i,j))
            if self.fly:
                dfs(n-i-1,m-1-j,path+1)
                self.fly-=1
            dfs(i-1,j,path+1)
            dfs(i+1,j,path+1)
            dfs(i,j-1,path+1)
            dfs(i,j+1,path+1)
            visited.remove((i, j))

        for i in range(n):
            for j in range(m):
                if matrix[i][j]=="S":
                   dfs(i,j,0)

        return self.min_path


if __name__=="__main__":
    s=Solution()
    matrix = [["#", "S", ".", "."], [".", "#", ".", "E"], ["#", ".", ".", "."], [".", ".", ".", "."]]
    print(s.minPath(matrix))