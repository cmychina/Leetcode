import random
class Sampleing:

    def PoolSampling(self,dataStream,m):
        receive=[0]*m
        n=len(dataStream)
        for i in range(m):
            receive[i]=dataStream[i]
        for i in range(m,n):
            d=random.choice(range(i+1))
            if d<m:
                receive[d]=dataStream[i]
        return receive
