def maxPalindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    for i in range(n):
        dp[i][i] = 1
        for j in range(i - 1, -1, -1):
            if s[j] == s[i]:
                dp[j][i] = 2 + dp[j + 1][i - 1]
            else:
                dp[j][i] = max(dp[j + 1][i], dp[j][i - 1])

    return dp[0][n - 1]