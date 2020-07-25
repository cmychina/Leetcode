"""
1.所在天数
2.剩余交易次数
3.持有状态
dp[i][k][0 or 1]
买进算一次交易
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
"""


#1.不限定交易次数
def maxProfit(prices):
    if not prices:
        return 0
    n=len(prices)
    dp=[[0]*2]*n
    dp[0][1]=-prices[0]
    for i in range(1,n):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
        dp[i][1]=max(dp[i-1][1],-prices[i])
    return dp[n-1][0]


#2.限定k=2次交易
def maxProfit(prices):
    if not prices:
        return 0
    n=len(prices)
    dp=[[[0]*2 for _ in range(3)] for _ in range(n)]
    for k in range(3):
        dp[0][k][1]=-float('inf')
    for i in range(n):
        dp[i][0][1]=-float('inf')
    dp[0][1][1]=-prices[0]
    for i in range(1,n):
        for k in range(1,3):
            dp[i][k][0]=max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
            dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
    return max(dp[n-1][1][0],dp[n-1][2][0])

#3.含冷冻期
def maxProfit(prices):
    if not prices:
        return 0
    n=len(prices)
    dp=[[0]*2 for _ in range(n)]
    dp[0][0]=0
    dp[0][1]=-prices[0]
    for i in range(1,n):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
        #i-2天卖出,i-1冷冻,i购入
        dp[i][1]=max(dp[i-1][1],dp[i-2][0]-prices[i])
    return dp[n-1][0]

#4.手续费
def maxProfit(prices,fee):
    if not prices:
        return 0
    n = len(prices)
    dp = [[0] * 2] * n
    dp[0][1] = -prices[0] - fee  ##初始持有股票的收益
    dp[0][0] = 0
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)  ##buy
    return dp[n - 1][0]
