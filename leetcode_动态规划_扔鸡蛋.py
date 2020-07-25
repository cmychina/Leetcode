
"""
dp[k][m]=n 表示k个鸡蛋，最多允许扔m次，最坏情况下最多可以度量n层
dp[k][m]=dp[k][m-1]+dp[k-1][m-1]+1
"""
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp=[[0]*(N+1) for _ in range(K+1)]
        m=0
        while dp[K][m] < N:
            m+=1
            for k in range(K,0,-1):
                dp[k][m]=dp[k-1][m-1]+dp[k][m-1]+1
        return m


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        memo = dict()

        def dp(N, K):
            if N == 0:
                return 0
            # 只有一个鸡蛋，只能线性扫描
            if K == 1:
                return N
            if (N, K) in memo:
                return memo[(N, K)]
            res = float('inf')
            for i in range(1, N + 1):
                res = min(res, max(dp(i - 1, K - 1), dp(N - i, K)) + 1)
            memo[(N, K)] = res
            return res

        return dp(N, K)

if __name__ == "__main__":
    s = Solution()

    T = "ABC"