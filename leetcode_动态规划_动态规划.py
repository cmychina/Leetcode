class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        n, m = len(dungeon), len(dungeon[0])
        BIG = 10**9
        dp = [[BIG] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)

        return dp[0][0]



    def Mudane(self,dungeon):
        M=len(dungeon)
        N=len(dungeon[0])
        #dp[i][j]表示达到(i,j)需要的最低健康点数
        dp=[[0]*N for _ in range(M)]
        dp[-1][-1]=max(1,1-dungeon[-1][-1])

        for i in range(N-2,-1,-1):
            dp[-1][i]=max(1,dp[-1][i+1]-dungeon[-1][i])
        for i in range(M-2,-1,-1):
            dp[i][-1]=max(1,dp[i+1][-1]-dungeon[i][-1])

        for i in range(M-2,-1,-1):
            for j in range(N-2,-1,-1):
                dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        print(dp)
        return dp[0][0]
if __name__=="__main__":
    S=Solution()
    m= [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(S.calculateMinimumHP(m))