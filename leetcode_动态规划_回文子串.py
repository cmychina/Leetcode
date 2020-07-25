"""
中心扩散
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        L = len(s)
        cnt = 0
        # 以某一个元素为中心的奇数长度的回文串的情况
        for center in range(L):
            left = right = center
            while left >= 0 and right < L and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
        # 以某对元素为中心的偶数长度的回文串的情况
        for left in range(L - 1):
            right = left + 1
            while left >= 0 and right < L and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1

        return cnt

class Solution:
    def countSubstrings(self, s: str) -> int:
        N= len(s)
        if N== 0 or s is None:
            return 0
        res = 0
        dp = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = True
        for j in range(N):
            for i in range(0, j):
                if j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
        for i in range(N):
            for j in range(i, N):
                if dp[i][j] is True:
                    res += 1
        return res
