"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

思路，构建堆，每次弹出最小的值，第k个被弹出的就是我们需要的数字。

"""
import heapq
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        N = len(matrix)
        # heap = [(matrix[i][0], i, 0) for i in range(n)]
        # heapq.heapify(heap)
        heap=[]
        for i in range(N):
            heapq.heappush(heap,(matrix[i][0],i,0))
        for i in range(k - 1):
            num, x, y = heapq.heappop(heap)
            #把其下一个加进来
            if y != N - 1:
                heapq.heappush(heap, (matrix[x][y + 1], x, y + 1))
        return heapq.heappop(heap)[0]
#时间复杂度 O(klogn)，归并k次，每次堆中插入和弹出的操作时间复杂度均为logN。

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)
        def check(mid):
            i, j = n - 1, 0
            res = 0
            while i >= 0 and j < n:
                if mid >= matrix[i][j]:
                    res += i + 1
                    j += 1
                else:
                    i -= 1
            return res >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

#时间复杂度：O(nlog(r−l))，二分查找进行次数为 O(log(r−l))，每次操作时间复杂度为O(n)。



