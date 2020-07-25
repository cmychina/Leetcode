class Solution:

    def topKFrequent(self, words, k: int):
        from collections import defaultdict
        cnt = defaultdict(int)
        for i in words:
            cnt.setdefault(i, 0)
            cnt[i] += 1

        sort_cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
        res = []
        for i in range(k):
            res.append(sort_cnt[i][0])
        return res