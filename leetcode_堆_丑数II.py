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

#dp+三指针
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        # 三指针初始化
        i2 = 0
        i3 = 0
        i5 = 0
        for i in range(1,n):
            min_val = min(dp[i2]*2,dp[i3]*3,dp[i5]*5)
            dp[i] = min_val
            # 找出哪个指针对应的数造出了现在这个最小值，将指针前移一位
            if dp[i2]*2 == min_val:
                i2 += 1
            if dp[i3]*3 == min_val:
                i3 += 1
            if dp[i5]*5 == min_val:
                i5 += 1
        return dp[-1]