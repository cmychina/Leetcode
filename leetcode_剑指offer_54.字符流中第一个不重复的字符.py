class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.cnt = {}
    def FirstAppearingOnce(self):
        # write code here
        for c in self.s:
            if self.cnt[c]==1:
                return c
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        self.cnt[char] = self.cnt.get(char, 0) + 1

class Solution:
    def __init__(self):
        self.s = ''
        self.queue = []  # 按顺序保存所有只出现一次的字符
        self.second = []  # 按顺序保存所有出现过的字符

    def FirstAppearingOnce(self):
        if self.queue:
            return self.queue[0]
        return '#'

    def Insert(self, char):
        self.s += char
        if char in self.queue:
            self.queue.pop(self.queue.index(char))
        elif char not in self.second:
            self.queue.append(char)
            self.second.append(char)