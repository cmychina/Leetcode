"""
思路：条件要满足 1）车从i站能开到i+1，2）所有站里的油总量要>=车子的总耗油量。
假设从编号为0站开始，一直到k站都正常，在开往k+1站时车子没油了。
这时，应该将起点设置为k+1站。
"""
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        N=len(gas)
        cand=[]
        for i in range(N):
            if gas[i]>=cost[i]:
                flag=i
                nxt=gas[i]-cost[i]
                while nxt+gas[(i+1)%N]>=cost[(i+1)%N]:
                    nxt=nxt+gas[(i+1)%N]-cost[(i+1)%N]
                    i+=1
                    i=i%N
                    if i==flag:
                        return i
        return -1

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost):
            return -1
        N,res,cur = len(gas),0,0
        for i in range(N):
            if cur < 0:
                res = i
                cur = 0
            cur += gas[i] - cost[i]
        return res