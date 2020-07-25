"""
hard
"""
#思路1 直接排序 nlogn
#思路2 大小堆   logn
import heapq
class MedianFinder:
    """
    最大堆中的所有数字都小于或等于最大堆的top元素
    最小堆中的所有数字都大于或等于最小堆的top元素
    大顶堆实现前有序数组中的最大值
    小顶堆实现后有序数组中的最小值
    为偶数，就两者均衡，为奇数，就让大顶堆元素比小顶堆多一即可(反过来也行)

    为了找到添加新数据以后，数据流的中位数，我们让这个新数据在大顶堆和小顶堆中都走了一遍。
    而为了让大顶堆的元素多 1 个，我们让从小顶堆中又拿出一个元素“送回”给大顶堆；
    同时保证小顶堆的顶大于大顶堆的顶

    下面的实现过程是保证小顶堆比大顶堆多一个值
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 初始化大顶堆和小顶堆
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        #保证小顶堆比大大顶推多一个元素
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        #此时大顶堆元素较少，加在大顶堆
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]

