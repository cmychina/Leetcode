"""
此处思路使用堆，时间复杂度NlogM
N表示所有元素，M表示行数
"""
import heapq
class Solution:
    def Find(self, target, array):
        M=len(array)
        N=len(array[0])
        if M*N==0:
            return False
        heap=[]
        for i in range(M):
            heapq.heappush(heap,(array[i][0],i,0))
        while heap:
            cur,x,y=heapq.heappop(heap)
            if cur==target:
                return True
            elif cur>target:
                break
            else:
                nx,ny=x,y+1
                if 0<=nx<M and 0<=ny<N:
                    heapq.heappush(heap,(array[nx][ny],nx,ny))
                else:
                    continue
        return False