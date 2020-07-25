"""
O(N)
找某点处左右最大值即可
"""
from typing import List
#dp
class Solution:
    def trap(self, height: List[int]) -> int:
        # 边界条件
        if not height:
            return 0
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        ans = 0
        # 初始化
        maxleft[0] = height[0]
        maxright[n-1] = height[n-1]
        # 设置备忘录，分别存储左边和右边最高的柱子高度
        for i in range(1,n):
            maxleft[i] = max(height[i],maxleft[i-1])
        for j in range(n-2,-1,-1):
            maxright[j] = max(height[j],maxright[j+1])
        # 一趟遍历，比较每个位置可以存储多少水
        for i in range(n):
            if min(maxleft[i],maxright[i]) > height[i]:
                ans += min(maxleft[i],maxright[i]) - height[i]
        return ans
#栈
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0
        res, idx = 0, 0
        stack = []
        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()  # index of the last element in the stack
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += (dist * h)
            stack.append(idx)
            idx += 1
        return res
#数学
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left,right=0,n-1
        SUM,tmp,high=0,0,1
        while(left<=right):
            while(left<=right and height[left]<high):
                SUM+=height[left]
                left+=1
            while(right>=left and height[right]<high):
                SUM+=height[right]
                right-=1
            high+=1
            tmp+=right-left+1
        return tmp-SUM
