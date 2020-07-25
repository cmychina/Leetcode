def uniquePathsWithObstacles(obstacleGrid):
    m=len(obstacleGrid)
    n=len(obstacleGrid[0])
    #起点与终点的限制
    if obstacleGrid[0][0] == 1:
        return 0
    if obstacleGrid[m-1][n-1] == 1:
        return 0
    #初始点无障碍，则初始化为1
    obstacleGrid[0][0] = 1
    #初始化行列
    #对于每行的第一个点，只要当前为0且上一行的点为1则设置为1,表示可以走到，否则设置0。
    for i in range(1,m):
        obstacleGrid[i][0]=int(obstacleGrid[i][0]==0 and obstacleGrid[i-1][0]==1)
    for j in range(1, n):
        obstacleGrid[0][j]=int(obstacleGrid[0][j]==0 and obstacleGrid[0][j-1]==1)
    #从(1,1)点开始遍历
    for i in range(1,m):
        for j in range(1,n):
            #0表示无障碍
            if obstacleGrid[i][j] == 0:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
            #有障碍设置为0，表示无路径通过
            else:
                obstacleGrid[i][j] = 0
    return obstacleGrid[m-1][n-1]


    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [1] + [0] * n
    for i in range(0, m):
        for j in range(0, n):
            dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
    return dp[-2]