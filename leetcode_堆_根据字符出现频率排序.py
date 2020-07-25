import heapq
import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        # 大顶堆
        countFrequency=collections.Counter(s)
        heap = []
        heapq.heapify(heap)
        for i in countFrequency:
            for j in range(countFrequency[i]):
                heapq.heappush(heap, (-countFrequency[i], i))

        return ''.join([heapq.heappop(heap)[1] for _ in range(len(s))])


