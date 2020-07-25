"""
思路：如果左括号数量不大于n，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号。
"""
class Solution:
    def generateParenthesis(self, n: int):
        if n==0:
            return[""]
        if n==1:
            return["()"]
        if n==2:
            return ["()()","(())"]
        result=[]
        for i in range(n):
            j=n-1-i
            tmp1=self.generateParenthesis(i)
            tmp2=self.generateParenthesis(j)
            result.extend(["({}){}".format(p,q)for p in tmp1 for q in tmp2])
        return result

class Solution:
    def generateParenthesis(self, n: int):

        res = []
        cur_str = ''

        def dfs(cur_str, left, right, n):

            if left == n and right == n:
                res.append(cur_str)
                return
            if left < right:
                return
            if left < n:
                dfs(cur_str + '(', left + 1, right, n)
            if right < n:
                dfs(cur_str + ')', left, right + 1, n)

        dfs(cur_str, 0, 0, n)
        return res


class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()
        backtrack([], 0, 0)
        return ans

