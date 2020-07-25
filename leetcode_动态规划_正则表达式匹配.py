def isMatchdp(s,p):
    S=len(s)
    P=len(p)
    dp = [[False] * (P + 1) for _ in range(S + 1)]
    dp[0][0]=True
    #初始化
    for i in range(P):
        if p[i]=="*" and dp[0][i-1]:
            dp[0][i+1]=True
    for i in range(S):
        for j in range(P):
            if p[j]==s[i] or p[j] in {s[i],"."}:
                dp[i+1][j+1]=dp[i][j]
            elif p[j]=="*":
                if p[j-1]!=s[i]:
                    dp[i+1][j+1]=dp[i+1][j-1]
                if p[i-1]==s[i] or p[j-1]==".":
                    dp[i+1][j+1]=(dp[i][j+1] or dp[i+1][j] or dp[i+1][j-1])
    return dp[-1][-1]

def isMatch(s, p):
    S = len(s)
    P = len(p)
    memo = {}

    def dp(i, j):
        if ((i, j) in memo):
            return memo[(i, j)]
        if (j == P):
            return i == S
        #当前是否匹配
        pre = i < S and p[j] in {s[i], "."}
        if (j <= P - 2 and p[j + 1] == "*"):
            #dp(i,j+2)表示*匹配前面0个，dp(1+1,j)表示匹配1个或多个
            tmp = dp(i, j + 2) or pre and dp(i + 1, j)
        # else:
        #     tmp = pre and dp(i + 1, j + 1)
        memo[(i, j)] = tmp
        return tmp

    return dp(0, 0)

s = "aa"
p = "a*"
print(isMatchdp(s,p))
print(isMatch(s,p))