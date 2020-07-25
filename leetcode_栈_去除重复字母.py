"""
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = {}
        for c in s:  # 字符计数
            counts[c] = counts.get(c, 0) + 1

        stack, stacked = [], set()
        for c in s:
            if c not in stacked:
                while stack and c < stack[-1] and counts[stack[-1]]:  # 当栈顶在后面还有且大于当前字符时弹出
                    stacked.remove(stack.pop())
                stack.append(c)
                print(stack)
                stacked.add(c)
            counts[c] -= 1
        return ''.join(stack)