class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for (u, v, w) in times:
            graph[u].append((v, w))
        #表示startNode到达i的距离
        dist = [float('inf')] * (N + 1)
        dist[0] = -1
        #记录已经访问过的点
        visited = set()
        #起始点
        dist[K] = 0
        while len(visited) < N:
            select_vertex = -1
            init_dist = float('inf')
            for i in range(1, N + 1):
                if i not in visited and dist[i] < init_dist:
                    select_vertex = i
                    init_dist = dist[i]
            if select_vertex == -1:
                break
            visited.add(select_vertex)
            for v, w in graph.get(select_vertex, []):
                if w + init_dist < dist[v]:
                    dist[v] = w + init_dist
        if max(dist) == float('inf'):
            return -1
        return max(dist)

import collections
import heapq
#Dijkstra算法 迪杰斯特拉
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {node: float('inf') for node in range(1, N+1)}
        seen = [False] * (N+1)
        #起始点
        dist[K] = 0
        while True:
            cand_node = -1
            cand_dist = float('inf')
            #找邻域那个距离最近的点
            for i in range(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i
            if cand_node < 0:
                break
            seen[cand_node] = True
            #找该节点的最近邻近点
            for neighbor, d in graph[cand_node]:
                dist[neighbor] = min(dist[neighbor], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1

#堆NlogN
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        heap = [(0, K)]
        dist = {}
        while heap:
            d, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = d
            for neighbor, d2 in graph[node]:
                if neighbor not in dist:
                    #d+d2会自动去排序
                    heapq.heappush(heap, (d+d2, neighbor))
        return max(dist.values()) if len(dist) == N else -1

