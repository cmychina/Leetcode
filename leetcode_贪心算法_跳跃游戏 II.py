class Solution:
    def jump(self,nums):
        N=len(nums)
        dp=[0]*N
        if N==0:
            return 0
        for i in range(N-1):
            for j in range(nums[i],0,-1):
                if i+j>=N-1:
                    return dp[i]+1
                elif dp[i+j]==0:
                    dp[i+j]=dp[i]+1
                else:
                    break


class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                #当前可以到达最远的位置
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
