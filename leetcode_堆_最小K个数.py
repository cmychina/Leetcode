"""
最小k个数用大顶堆
"""
class Solution:
    def smallestK(self, arr, k: int):

        import heapq
        heap=[]
        if k==0:
            return []
        for num in arr:
            if len(heap)<k:
                heapq.heappush(heap,-num)
            elif -num>heap[0]:
                heapq.heapreplace(heap,-num)
        return [-heapq.heappop(heap) for _ in range(k) ]