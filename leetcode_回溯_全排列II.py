class Solution:
    """
    包含重复数字的，返回所有不重复的排列
    """
    def permuteUnique(self, nums):
        n = len(nums)
        res = []
        visited = set()
        def dfs(tmp):
            if len(tmp) == n:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i in visited or (i>0 and i-1 not in visited and nums[i]==nums[i-1]):
                    continue
                visited.add(i)
                dfs(tmp + [nums[i]])
                visited.remove(i)

        dfs([])
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 2]
    print(s.permuteUnique(nums))