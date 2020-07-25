"""
顺时针打印数组
"""
def funx():
    r, i, j, di, dj = [], 0, 0, 0, 1
    if matrix != []:
        for _ in range(len(matrix) * len(matrix[0])):
            r.append(matrix[i][j])
            matrix[i][j] = 0
            if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
                di, dj = dj, -di
            i += di
            j += dj
    return r

class solution:
    def printMatrix(self,matrix):
        if not matrix:
            return []
        n=len(matrix)
        m=len(matrix[0])
        left,right=0,m-1
        bottom,top=n-1, 0
        res=[]
        while True:
            for i in range(left,right+1):
                res.append(matrix[left][i])
            top+=1
            if top>bottom:
                break
            for i in range(top,bottom+1):
                res.append(matrix[i][right])

            right-=1
            if right<left:
                break
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom-=1
            if top > bottom:
                break

            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            if right < left:
                break
        return res

if __name__=="__main__":
    s=solution()
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    print(s.printMatrix(matrix))
