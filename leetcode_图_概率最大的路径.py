import  collections
from typing import List
import math
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        import heapq
        graph = collections.defaultdict(dict)
        for i, edge in enumerate(edges):
            a, b = edge
            graph[a][b] = succProb[i]
            graph[b][a] = succProb[i]
        heap = [(-1, start)]
        visited = set()
        while heap:
            prob, node = heapq.heappop(heap)
            if node == end:
                return -prob
            visited.add(node)
            for nxt in graph[node]:
                if nxt not in visited:
                    #大顶堆
                    heapq.heappush(heap, (prob * graph[node][nxt], nxt))
        return 0

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for i, edge in enumerate(edges):
            a, b = edge
            graph[a][b] = succProb[i]
            graph[b][a] = succProb[i]

        heap = [(-1, start)]
        dist = collections.defaultdict(float)
        dist[start] = -1
        while heap:
            curdist, cur = heapq.heappop(heap)
            if cur == end:
                return -curdist
            for node, prob in graph[cur]:
                tmp = curdist * prob
                if tmp < dist[node]:
                    dist[node] = tmp
                    heapq.heappush(heap, (tmp, node))
        return 0

