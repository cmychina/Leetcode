class Solution:
    def canJump(self, nums) -> bool:
        n=len(nums)
        dp=[False]*n
        dp[0]=True
        for i in range(1,n):
            if nums[i]<nums[i-1] and nums[i-1]>1:
                nums[i]=nums[i-1]-1
            dp[i]=dp[i-1] and nums[i-1]>0
        return dp[-1]

class Solution:
    def canJump(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i

