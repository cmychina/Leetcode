"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
"""
class Solution:
    def longestValidParentheses(self, s):
        stack=[-1]
        max_len=float("-inf")
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                #此时空栈说明是第一个右括号
                if not stack:

                    stack.append(i)
                max_len=max(max_len,i-stack[-1])
        return max_len

    def Mundane(self,s):
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        res = 0
        for i in range(n):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                # i-dp[i-1]-1表示与i处右括号匹配的左括号的位置
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]

        return dp

if __name__ == "__main__":
    s = Solution()
    w1="()()))"
    #print(s.longestValidParentheses(w1))
    print(s.Mundane(w1))