class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if(not s or s[0]=="0"):
            return 0
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(1,n):
            if(s[i]=="0"):
                if(s[i-1]=="1" or s[i-1]=="2"):
                    dp[i+1]=dp[i-1]
                else:
                    return 0
            else:#s[i]!=0
                if(s[i-1]=="1" or (s[i-1]=="2" and "1"<=s[i]<="6")):
                    dp[i+1]=dp[i]+dp[i-1]
                else:
                    dp[i+1]=dp[i]
        return dp[-1]


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [1, 0]
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(1, n):
            dp.append(0)
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if s[i - 1:i + 1] >= '10' and s[i - 1:i + 1] <= '26':
                dp[i + 1] += dp[i - 1]

        return dp[-1]