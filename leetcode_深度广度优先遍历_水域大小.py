class Solution:
    def pondSizes(self, land):
        M=len(land)
        N=len(land[0])
        res=[]
        def dfs(i,j):
            if not (0<=i<M and 0<=j<N and land[i][j]==0):
                return 0
            land[i][j]=1
            k=1
            #上下左右
            k+=dfs(i+1,j)
            k+=dfs(i-1,j)
            k+=dfs(i,j+1)
            k+=dfs(i,j-1)
            #对角线
            k+=dfs(i-1,j-1)
            k+=dfs(i+1,j+1)
            k+=dfs(i-1,j+1)
            k+=dfs(i+1,j-1)

            return k


        for i in range(M):
            for j in range(N):
                if land[i][j]==0:
                    k=dfs(i,j)
                    res.append(k)
        return sorted(res)


    def Mundane(self,land):

        M = len(land)
        N = len(land[0])
        res = []
        direction=[(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,-1),(-1,1),(-1,-1)]

        def dfs(x,y):
            k=1
            for dx,dy in direction:
                x_n=x+dx
                y_n=y+dy
                if 0<=x_n<M and  0<=y_n<N and land[x_n][y_n]==0:
                    land[x_n][y_n]=1
                    k+=dfs(x_n,y_n)
            return k


        for i in range(M):
            for j in range(N):
                if land[i][j]==0:
                    k=dfs(i,j)
                    res.append(k)
        return sorted(res)