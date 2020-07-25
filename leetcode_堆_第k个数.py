"""
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。
例如，前几个数按顺序应该是 1，3，5，7，9，15，21。
"""
#同丑数
import heapq
class Solution:
    """
     使用最小堆排序，时间复杂度O(nlogn)，空间复杂度O(2n)
    """
    def nthUglyNumber(self, k):

        heap = [1]
        visited = set([1])
        heapq.heapify(heap)
        nth = 0
        for i in range(k):
            nth = heapq.heappop(heap)  # 取出第i个丑数
            for j in [2, 3, 5]:
                cur= nth * j
                if cur not in visited:
                    visited.add(cur)
                    heapq.heappush(heap, cur)
        return nth