class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return "0"
        stack=[]
        n=len(num)
        for i in range(n):
            while stack and k and stack[-1]>num[i]:#开始出现逆序
                stack.pop()
                k-=1
            stack.append(num[i])
        while k:
            stack.pop()
            k -=1
        res=""
        for i in range(len(stack)):
            if stack[i]=="0" and res=="":
                continue
            res+=stack[i]
        return "0" if res=="" else res