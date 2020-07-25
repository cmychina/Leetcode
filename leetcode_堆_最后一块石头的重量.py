class Solution:
    def lastStoneWeight(self, stones) -> int:
        """
        搞一个大顶推
        """
        import heapq
        import numpy as np
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while heap:
            cur=-heapq.heappop(heap)
            if not heap:
                return cur
            next=-heapq.heappop(heap)
            ans=cur-next
            heapq.heappush(heap,-ans)
        return ans
