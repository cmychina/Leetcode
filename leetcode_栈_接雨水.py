"""
给定 n个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
关键：一个位置能容下的雨水量等于它左右两边柱子最大高度的最小值减去它的高度
"""
class Solution:
    def trap(self, height) -> int:
        #栈
        if not height:
            return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:#维护一个高度递减的栈
                tmp = stack.pop()
                if not stack:
                    break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i-stack[-1] - 1)
            stack.append(i)
        return res

        #动态规划
        if not height:
            return 0
        n=len(height)
        max_height_left=[0]*n
        max_height_right=[0]*n
        max_height_left[0]=height[0]
        max_height_right[-1]=height[-1]
        for i in range(1,n):
            max_height_left[i]=max(height[i],max_height_left[i-1])
        for j in range(n-2,-1,-1):
            max_height_right[j]=max(height[j],max_height_right[j+1])
        res=0
        for i in range(n):
            res+=min(max_height_left[i],max_height_right[i])-height[i]
        return res