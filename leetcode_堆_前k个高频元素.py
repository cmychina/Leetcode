"""
topk （前k大）用小根堆，维护堆大小不超过 k 即可。
每次压入堆前和堆顶元素比较，如果比堆顶元素还小，直接扔掉，否则压入堆。
检查堆大小是否超过 k，如果超过，弹出堆顶。复杂度是 nlogk
heapreplace(a,x)返回最初在a中的最小值,而不管x的值如何,顾名思义,
heappushpop(a,x)在弹出最小值之前将x推送到a上
"""

import collections
import heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        heap = []
        col = collections.Counter(nums)
        print(col)
        #这里面堆可以是一个元组，前者表示频数，后者表示数
        for num, v in col.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (v, num))
            else:
                heapq.heappush(heap, (v, num))
        return [ele[1] for ele in heap]