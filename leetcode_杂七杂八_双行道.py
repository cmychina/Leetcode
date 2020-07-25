
n=input()
matrix=[[0]*int(n) for _ in range(2)]
first=input()
second=input()
for i in range(int(n)):
    matrix[0][i]=first[i]
    matrix[1][i] = second[i]

def getpath(matrix):
    if not matrix:
        return 0
    if matrix[0][0]=="X":
        return 0
    if matrix[-1][-1]=="X":
        return 0

    col=len(matrix[0])
    dp = [[0] * col for _ in range(4)]

    dp[1][0] = 1
    for j in range(1, col):
        for i in range(2):
            if matrix[i][j] != "X":
                dp[i+1][j] = dp[i+1][j - 1] + dp[i + 2][j - 1] + dp[i][j - 1]
    print(dp)
    return dp[2][-1]

if __name__=="__main__":
    import sys
    #print(matrix)
    ans=getpath(matrix)
    sys.stdout.write(str(ans))
    """
    5
    ..X.X
    XX...
    """