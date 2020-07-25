
"""
至多包含两个不同字符的最长子串
"""
class solution:
    def Mundane(self,s):
        from collections import defaultdict
        start=0
        end=0
        lookup=defaultdict(int)
        max_len=0
        n=len(s)
        counter=0

        while end<n:
            #之前没出现过，说明是新字母
            if lookup[s[end]]==0:
                counter+=1
            lookup[s[end]]+=1
            end+=1

            while counter>2:
                #只剩1个字母了，此次迭代就可以减少一个字母
                if lookup[s[start]]==1:
                    counter-=1
                lookup[s[start]]-=1
                start+=1
            max_len=max(max_len,end-start)
        return max_len

if __name__ == "__main__":
    s = solution()
    str="ccaabbb"
    print(s.Mundane(str))




