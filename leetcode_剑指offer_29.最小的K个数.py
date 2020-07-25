class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        """
        最大堆
        :param tinput:
        :param k:
        :return:
        """
        import heapq
        heap = []
        if k == 0:
            return []
        for num in tinput:
            if len(heap) < k:
                heapq.heappush(heap, -num)
            elif -num > heap[0]:
                heapq.heapreplace(heap, -num)
        return [-heapq.heappop(heap) for _ in range(k)]
