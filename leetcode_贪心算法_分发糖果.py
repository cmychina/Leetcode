"""
初始化left和right [1] 然后依次遍历 最后取两种情况下的最大值，就能都满足条件
"""
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        left=[1]*n
        right=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        count=left[-1]
        for j in range(n-2,-1,-1):
            if ratings[j]>ratings[j+1]:
                right[j]=right[j+1]+1
            count+=max(left[j],right[j])
        return count