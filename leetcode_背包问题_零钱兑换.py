class Solution:
    def coinChange(self, coins, amount):

        #背包问题
        #dp[i]表示组成金额i所需要的最小硬币数
        N=len(coins)
        dp=[float("inf")]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin >=0:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[-1] if(dp[-1]!=float("inf")) else -1