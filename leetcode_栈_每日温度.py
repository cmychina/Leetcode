class Solution:
    def dailyTemperatures(self, T):
        n=len(T)
        res=[0]*n
        stack=[]
        for i in range(n):
            while stack and T[i]>T[stack[-1]]:
                res[stack.pop()]=i-stack[-1]
            stack.append(i)
        return res

if __name__ == "__main__":
    s = Solution()
    T=[73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(T))