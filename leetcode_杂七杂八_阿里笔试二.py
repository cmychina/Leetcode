


import sys
seq=[]
while 1:
    line=sys.stdin.readline().strip()
    if line=='':
        break
    seq.append(line)
num=seq[1:]
n=len(num)
#dp[i][j]表示两个字母之间的最大长度，dp[0][1]为以字符a为开头，字符b为结尾的最大长度，dp[0][25]表示以字符a为开头，字符z为结尾的最大长度
dp=[[0 for _ in range(26)] for _ in range(26)]
for i in range(n):
    tmp=num[i]
    for j in range(ord(tmp[0])-97+1):#ord('a')=97
        for k in range(25,ord(tmp[-1])-97-1,-1):
            dp[j][k]=max(dp[j][k],dp[j][ord(tmp[0])-97]+dp[ord(tmp[-1])-97][k]+len(tmp))
print(dp)


import sys
seq=[]
while 1:
    line=sys.stdin.readline().strip()
    if line=='':
        break
    seq.append(line)
nums=seq[1:]
n=len(nums)
nums.sort(key=lambda x:(x[-1],x[0]))
print(nums)
#dp[j]表示 a~'j'之间的最大长度
dp=[0]*26
for i in range(n):
    tmp=nums[i]
    tmp_length=len(tmp)
    left=ord(tmp[0])-ord('a')
    right=ord(tmp[-1])-ord('a')
    left_max=0
    for j in range(left+1):
        left_max=max(dp[j],left_max)
        dp[right]=max(dp[right],left_max+tmp_length)
print(dp)

