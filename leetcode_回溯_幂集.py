class Solution:
    def subsets(self, nums):
        n=len(nums)
        res=[]
        def backtrack(i,tmp):
            res.append(tmp)
            for j in range(i,n):
                backtrack(j+1,tmp+[nums[j]])
        backtrack(0,[])
        return res