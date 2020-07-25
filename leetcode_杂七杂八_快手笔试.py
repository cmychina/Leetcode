
import sys
import collections
import torch

def genSeq(values):
    count = collections.defaultdict(int)
    s, a, b, p = values[0], values[1], values[2], values[3]
    arr = []
    arr.append(s)
    count[s] = 1
    i = 1
    while 1:
        x = (arr[i - 1] * a + b) % p
        if count[x] == 2:
            arr = arr[:i]
            break
        else:
            arr.append(x)
            count[x] += 1
            i += 1
    del count
    return arr


def getMaxlen(arr1, arr2):
    ##求最大公共子序列长度
    n = len(arr1)
    m = len(arr2)
    ##dp[i][j]表示arr1[0]~arr1[i]与arr2[0]~arr2[j]之间的最长公共子序列长度
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if arr1[i] == arr2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[-1][-1]



if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    seq = []
    for i in range(2 * T):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        seq.append(values)
    for i in range(0,2*T,2):
        seq1=seq[i]
        seq2=seq[i+1]
        if seq1==seq2:
            print(len(genSeq(seq1)))
        else:
            print(getMaxlen(genSeq(seq1),genSeq(seq2)))















'''
class Solution:
    def find_best_path_cost(self , A ):
        n=len(A)
        m=len(A[0])

        for i in range(1,n):
            A[i][0]=A[i-1][0]+A[i][0]
        for j in range(1,m):
            A[0][j]=A[0][j-1]+A[0][j]

        for i in range(1,n):
            for j in range(1,m):
                A[i][j]=min(A[i-1][j],A[i][j-1])+A[i][j]
        print(A[-1][-1])




if __name__=='__main__':
    s=Solution()
    A=[[1,2,3],[4,5,6],[7,8,9]]
    print(s.find_best_path_cost(A))



import sys
line=sys.stdin.readline().strip().split()
K=int(line[0])
N=int(line[1])

res=1
while K:
    div=N//K
    res*=div
    N-=div
    K-=1
print(res)
'''



