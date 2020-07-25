
class solution:

    def Mundane(self,s,t):
        from collections import defaultdict
        lookup=defaultdict(int)
        #先计算t中的字符个数
        for c in t:
            lookup[c]+=1
        start=0
        end=0
        min_len=float("inf")
        counter=len(t)
        res=""
        while end<len(s):
            #该字母在t中
            if lookup[s[end]]>0:
                counter-=1
            lookup[s[end]]-=1
            end+=1
            #说明当前start-end包含了t
            while counter==0:
                if min_len>end-start:
                    min_len=end-start
                    res=s[start:end]
                #最左边的数字
                if lookup[s[start]]==0:
                    counter+=1
                lookup[s[start]]+=1
                start+=1
        return res


if __name__ == "__main__":
    s = solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    print(s.Mundane(S,T))


