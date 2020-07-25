class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        N=len(numbers)
        for i in range(N):
            if numbers[i]<0 or numbers[i]>N-1:
                return False
        for i in range(N):
            while numbers[i]!=i:
                if numbers[i]==numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                numbers[i],numbers[numbers[i]]=numbers[numbers[i]],numbers[i]
                print(numbers)
                break
        return False
if __name__=="__main__":
    s=Solution()
    numbers=[2,3,1,0,2,5,3]
    duplication=[0]
    print(s.duplicate(numbers,duplication))
