class Solution:

    def wordBreak(self, s: str, wordDict) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp


    def Mundane(self,s,wordDict):
        n = len(s)
        if not wordDict: return not s
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]



if __name__=="__main__":
    S=Solution()

    s = "catsandog"
    wordDict = ["cats", "and", "og"]
    print(S.wordBreak(s,wordDict))