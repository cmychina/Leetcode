"""
S = "qqe"
["eqq","qeq","qqe"]

"""

class Solution:
    def permutation(self, S: str):
        S = sorted(S)
        n=len(S)
        res = []
        seen = [0] * len(S)

        def back(tmp):
            if len(tmp) == n:
                res.append(tmp)
                return
            for j in range(n):
                if seen[j]:
                    continue
                #注意此处约束
                if j > 0 and S[j] == S[j-1] and not seen[j-1]:
                    continue
                seen[j] = 1
                back(tmp+S[j])
                seen[j] = 0

        back("")
        return res

