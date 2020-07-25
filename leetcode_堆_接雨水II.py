from typing import List
import heapq
class Solution:  # 优先队列 小顶堆 + bfs （围栏法）
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap:
            return 0
        heap, visited = [], set()
        m, n = len(heightMap), len(heightMap[0])
        for i in range(m):
            heap.append((heightMap[i][0], i, 0))
            heap.append((heightMap[i][n - 1], i, n - 1))
            visited.add((i, 0))
            visited.add((i, n - 1))
        for j in range(n):
            heap.append((heightMap[0][j], 0, j))
            heap.append((heightMap[m - 1][j], m - 1, j))
            visited.add((0, j))
            visited.add((m - 1, j))

        heapq.heapify(heap)
        min_max = float('-inf')
        ans = 0
        #找最低的板，看周围是否可以填水
        while heap:
            h, i, j = heapq.heappop(heap)
            min_max = max(min_max, h)
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    if heightMap[x][y] < min_max:
                        ans += min_max - heightMap[x][y]
                    heapq.heappush(heap, (heightMap[x][y], x, y))
                    visited.add((x, y))
        return ans
