import heapq
import collections
class Solution:
    def topKFrequent(self, words, k: int):
        count = collections.Counter(words)
        #默认heap是小顶堆，因此频率取负数。
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
#nlogk

class Solution:
    def topKFrequent(self, words, k: int):
        import collections
        count = collections.Counter(words)
        count = list(count.items())
        count.sort(key=lambda x: (-x[1], x[0]))
        return list(map(lambda x: x[0], count))[:k]
#nlogn