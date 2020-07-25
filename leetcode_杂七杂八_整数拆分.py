class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(1,i):
                #j*(i-j)表示拆分成两个数的乘积
                #j*dp[i-j]表示拆分成多个数的乘积
                dp[i] = max(dp[i],j*(i-j),j*dp[i-j])
        return dp[n]
if __name__=="__main__":
    s=Solution()
    n=10
    print(s.integerBreak(n))