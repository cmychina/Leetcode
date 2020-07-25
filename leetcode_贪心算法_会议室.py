"""
思路1：将起始时间和结束时间一起排序，遍历，遇到起始时间，cur+1，结束时间 cur-1 统计出现过的最大cur
思路2：将会议结束时间保存再最小堆中，每次只要新会议开始时间小于时间，需要新房间，否则替代这个房间
"""
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        events = [(iv[0], 1) for iv in intervals] + [(iv[1], -1) for iv in intervals]
        events.sort()
        print(events)
        ans = cur = 0
        for _, e in events:
            cur += e
            ans = max(ans, cur)
        return ans

import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if len(intervals) == 0:
            return 0
        # 根据会议开始时间排序
        intervals.sort()
        rooms = [intervals[0][0]]   # 小顶堆保存最早的结束时间
        for s, e in intervals:
            if rooms[0] <= s:       # 当前最小结束时间小于当前开始时间
                heapq.heapreplace(rooms, e)
            else:                   # 没有空余房间
                heapq.heappush(rooms, e)
        return len(rooms)           # 返回房间个数