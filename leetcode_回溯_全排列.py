class Solution:
    """
    不包含重复数字的
    """
    def permute(self, nums):
        n=len(nums)
        res=[]
        visited=set()
        def dfs(tmp):
            if len(tmp)==n:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    dfs(tmp+[nums[i]])
                    visited.remove(nums[i])
        dfs([])
        return res





if __name__ == "__main__":
    s = Solution()
    nums=[1,2,3]
    print(s.permute(nums))