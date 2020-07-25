class Solution:
    def rob(self, nums) -> int:
        ##怎么让收尾不相连？？？？
        n = len(nums)
        if n == 0:
            return 0
        elif 1 <= n <= 3:
            return max(nums)

        else:
            ##不考虑最后一个
            dp1 = [0] * n
            dp1[0] = nums[0]
            dp1[1] = max(nums[0], nums[1])
            for i in range(2, n - 1):
                dp1[i] = max(nums[i] + dp1[i - 2], dp1[i - 1])

            # 不考虑第一个
            dp2 = [0] * n
            dp2[1] = nums[1]
            dp2[2] = max(nums[1], nums[2])
            for i in range(3, n):
                dp2[i] = max(nums[i] + dp2[i - 2], dp2[i - 1])
        return max(max(dp1), max(dp2))
