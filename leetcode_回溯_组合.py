"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
"""
class Solution:
    def combine(self, n, k):
        res = []
        def backtrack(i, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                backtrack(j + 1, tmp + [j])

        backtrack(1, [])
        return res





if __name__ == "__main__":
    s = Solution()
    n=4
    k=2
    print(s.combine(n,k))