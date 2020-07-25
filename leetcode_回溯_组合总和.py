"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
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
                backtrack(j,tmp+[candidates[j]])

        backtrack(0,[])
        return res
if __name__ == "__main__":
    s = Solution()
    nums = [2,3,6,7]
    target=7
    print(s.combinationSum(nums,target))
