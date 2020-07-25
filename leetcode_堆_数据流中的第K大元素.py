"""
维护一个大小为k的小根堆，这样堆顶的元素就是第K大元素
"""

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.minheap = []

        # 构建大小为 k 的小顶堆(O(k))
        for i in range(min(k, len(nums))):
            self.minheap.append(nums[i])
            self.sift_up(i)

        # 将多余的 nums 元素加入其中(O(nlog(t)))
        for num in nums[k:]:
            if num > self.minheap[0]:
                self.minheap[0] = num
                # 下沉新加入的节点以维护小顶堆
                self.sift_down(0, k - 1)

    def sift_up(self, new_idx: int):
        new_val = self.minheap[new_idx]
        # 循环比较新加入的节点以及其双亲节点以上浮新加入的节点
        while new_idx > 0 and new_val < self.minheap[(new_idx - 1) // 2]:
            self.minheap[new_idx] = self.minheap[(new_idx - 1) // 2]
            new_idx = (new_idx - 1) // 2
        self.minheap[new_idx] = new_val

    def sift_down(self, start, end):
        start_val = self.minheap[start]
        # 循环比较新加入的节点以及其双子节点以下沉新加入的节点
        while start * 2 + 1 <= end:
            child = start * 2 + 1
            # 找到双子节点中较小的一个节点
            if child + 1 <= end and self.minheap[child] > self.minheap[child + 1]:
                child += 1
            if start_val > self.minheap[child]:
                self.minheap[start] = self.minheap[child]
                start = child
            else:
                break
        self.minheap[start] = start_val

    def add(self, val):
        if len(self.minheap) < self.k:
            self.minheap.append(val)
            self.sift_up(len(self.minheap) - 1)
        elif self.minheap[0] < val:
            self.minheap[0] = val
            self.sift_down(0, self.k - 1)
        return self.minheap[0]


#便捷写法
import heapq
class KthLargest(object):

    def __init__(self, k, nums):

        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):

        #堆个数小于k，则添加
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        #最小元素小于新元素，替代
        elif self.heap[0] < val:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]
