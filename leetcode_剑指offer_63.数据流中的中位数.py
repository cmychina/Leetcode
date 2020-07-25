"""
思路，一个大顶堆一个小顶堆 大顶堆中的值小于小顶堆中的值
并且保持大顶堆和小顶堆均衡
下面代码是保持小顶堆>=大顶堆
"""
import heapq


class Solution:
    def __init__(self):

        self.minheap = []
        self.maxheap = []
        self.cnt = 0
        self.res = []

    def Insert(self, num):
        for i in num:
            # 两者均衡
            if len(self.minheap) == len(self.maxheap) == 0:
                heapq.heappush(self.maxheap, -i)
            elif len(self.minheap) == len(self.maxheap):
                if i < self.minheap[0]:
                    heapq.heappush(self.maxheap, -i)
                else:
                    heapq.heappush(self.maxheap, -(heapq.heappushpop(self.minheap, i)))

            elif i < -self.maxheap[0]:
                heapq.heappush(self.minheap, -(heapq.heappushpop(self.maxheap, -i)))
            else:
                heapq.heappush(self.minheap, i)

            self.cnt += 1
            # print(self.minheap)
            # print(self.maxheap)
            self.res.append(self.CalMedian())

    def CalMedian(self):
        if self.cnt % 2 == 0:
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            return -self.maxheap[0]

    def GetMedian(self):

        return self.res