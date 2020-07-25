class Solution:
    def findDiagonalOrder(self,matrix):
        from collections import defaultdict
        lookup=defaultdict(list)
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                lookup[i+j].append(matrix[i][j])
        #print(lookup)
        res=[]
        flag=True
        for k,v in sorted(lookup.items()):
            if flag:
                res.extend(v[::-1])
            else:
                res.extend(v)
            flag=not flag

        return res



if __name__=="__main__":
    s=Solution()
    matrix=[
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
    print(s.findDiagonalOrder(matrix))