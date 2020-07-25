"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
"""
class Solution:
    def combinationSum(self, candidates,target):
        candidates.sort()
        n=len(candidates)
        res=[]
        def backtrack(i,tmp):
            if sum(tmp)==target:
                res.append(tmp)
                return
            for j in range(i,n):
                if candidates[j]+sum(tmp)>target:
                    break
                if j>i and candidates[j]==candidates[j-1]:
                    print(j)
                    continue
                backtrack(j+1,tmp+[candidates[j]])

        backtrack(0,[])
        return res
if __name__ == "__main__":
    s = Solution()
    candidates = [10,1,2,7,6,1,5]
    target=8
    print(s.combinationSum(candidates,target))