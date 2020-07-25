"""
编写一段程序来查找第 n 个超级丑数
超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
n = 12, primes = [2,7,13,19]
"""
import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes):
        heap = []
        heapq.heappush(heap, 1)
        visited = set([1])
        cur = 0
        for _ in range(n):
            cur = heapq.heappop(heap)
            for p in primes:
                new = cur * p
                if new not in visited:
                    visited.add(new)
                    heapq.heappush(heap, new)
        return cur
