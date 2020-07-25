"""
如果求最小的k个数，那么使用"大根堆"，如果求最大的k个数，那么使用"小根堆"。
当求最小的k个数时，用堆来维护当前k个数中的最大值，那么若后来的数比最大值还大，那么显然不是候选答案，直接丢弃。
当求最大的k个数时，用堆来维护当前k个数中的最小值，那么若后来的数比最小值还小，那么显然不是候选答案，直接丢弃。
否则的话，弹出队列头部元素，后来的元素入队，然后仍然保持着上述性质。
这样的时间复杂度为O(n*logk)，解释这个复杂度：最坏的情况下，后进来的每个元素都要重新入优先队列，每个元素入队和队顶弹出复杂度是logk，这样一来就是n*logk。
由于logk很小，实际运行应该和O(n)差不多。
若排序，那么最快也是O(nlogn)的。
这里求得是最近的点，也就是求最小，那么使用"大根堆"。
"""
class Solution:
    def kClosest(self, points, K: int):
        import heapq
        import numpy as np
        heap=[]
        for point in points:
            x=point[0]
            y=point[1]
            dist=np.sqrt(x**2+y**2)
            heapq.heappush(heap,(dist,point))
        res=[heapq.heappop(heap)[1] for _ in range(K)]
        return res

#nlogn
#可以只维护一个k堆，最小值维度最大堆，nlogk
class Solution:
    def kClosest(self, points, K: int):
        import heapq
        import numpy as np
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = np.sqrt(x ** 2 + y ** 2)
            if len(heap) < K:
                heapq.heappush(heap, (-dist, point))
            elif -dist > heap[0][0]:
                    heapq.heapreplace(heap, (-dist, point))
        res = [heapq.heappop(heap)[1] for _ in range(K)]
        return res
