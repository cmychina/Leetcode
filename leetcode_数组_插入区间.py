class Solution:
    def insert(self,intervals,newInterval):
        intervals.append(newInterval)
        intervals = sorted(intervals)
        res = []
        n = len(intervals)
        i = 0
        while (i < n):
            left = intervals[i][0]
            right = intervals[i][1]
            while (i < n - 1 and intervals[i + 1][0] <= right):
                i = i + 1
                right = max(intervals[i][1], right)
            res.append([left, right])
            i = i + 1
        return res

    def insert2(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        res = []
        # 找左边重合区域
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        tmp = [newInterval[0], newInterval[1]]
        # 找右边重合区域
        while i < n and newInterval[1] >= intervals[i][0]:
            tmp[0] = min(tmp[0], intervals[i][0])
            tmp[1] = max(tmp[1], intervals[i][1])
            i += 1
        res.append(tmp)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
