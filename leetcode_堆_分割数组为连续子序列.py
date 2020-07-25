"""
字典的键为序列结尾数值，值为结尾为该数值的所有序列长度（以堆存储）。
更新方式：每遍历一个数，将该数加入能加入的长度最短的序列中，不能加入序列则新建一个序列；然后更新字典。
"""
import heapq
from collections import defaultdict
class Solution:
    def isPossible(self, nums):

        chains = defaultdict(list)
        for i in nums:
            if not chains[i - 1]:
                heapq.heappush(chains[i], 1)
            else:
                min_len = heapq.heappop(chains[i - 1])
                heapq.heappush(chains[i], min_len + 1)

        for _, chain in chains.items():
            if chain and chain[0] < 3:
                return False
        return True

