"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
dp[i][j]表示word1[:i]到word2[:j]之间操作需要的次数
插入一个字符 dp[i][j - 1]    插入一个和j相同的
删除一个字符 dp[i - 1][j]    把i的词删除掉
替换一个字符 dp[i - 1][j - 1] 即把i j 替换成相等的

"""
class Solution:
    def minDist(self,word1,word2):
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    w1="distance"
    w2="springbok"
    print(s.minDist(w1,w2))