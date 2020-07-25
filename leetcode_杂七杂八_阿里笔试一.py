
path=[]
def dfs(state):
    if tuple(state) in memo:
        return memo[tuple(state)]
    if sum(state) == 0:
        return 0
    else:
        res = float('inf')
        for i in range(10):
            # 出三连对子
            if i < 8 and state[i] > 1 and state[i + 1] > 1 and state[i + 2] > 1:
                state[i] -= 2
                state[i + 1] -= 2
                state[i + 2] -= 2
                res = min(res, dfs(state) + 1)
                state[i] += 2
                state[i + 1] += 2
                state[i + 2] += 2
                memo[tuple(state)] = res
            # 出顺子
            if i < 6 and state[i] > 0 and state[i + 1] > 0 and state[i + 2] > 0 and state[i + 3] > 0 and state[
                i + 4] > 0:
                state[i] -= 1
                state[i + 1] -= 1
                state[i + 2] -= 1
                state[i + 3] -= 1
                state[i + 4] -= 1
                res = min(res, dfs(state) + 1)
                state[i] += 1
                state[i + 1] += 1
                state[i + 2] += 1
                state[i + 3] += 1
                state[i + 4] += 1
                memo[tuple(state)] = res
            # 出2张对子
            if res == float('inf') and state[i] > 1:
                state[i] -= 2
                res = min(res, dfs(state) + 1)
                state[i] += 2
                memo[tuple(state)] = res
            # 单出一张
            if res == float('inf') and state[i] > 0:
                state[i] -= 1
                res = min(res, dfs(state)+1)
                state[i] += 1
                memo[tuple(state)] = res
        return res
memo = {}

state = [2,3,3,1,1,1,3,2,2,1]
import time
t=time.time()
print(dfs(state))
print(memo)
print(time.time()-t)



