"""
滑动窗口
"""
class solution:
    def lengthOfLongestSubstring(self,s):
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            #end表示当前遍历的指针
            if lookup[s[end]] > 0:#表示该字母在前面出现过
                counter += 1
            lookup[s[end]] += 1
            end += 1
            #出现重复数字，开始移动窗口
            while counter > 0:
                #找重复的数字
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len


    def Qili(self,s):
        from collections import defaultdict
        if not s:
            return 0
        left=0
        end=0
        n=len(s)
        lookup=defaultdict(int)
        max_len=0
        counter=0
        while end<n:
            #出现重复
            if lookup[s[end]]>0:
                counter+=1
            lookup[s[end]]+=1
            end+=1
            while counter>0:
                #找到重复
                if lookup[s[left]]>1:
                    counter-=1
                lookup[s[left]]-=1
                left+=1

            max_len=max(max_len,end-left)
        return max_len

    def Mundane(self,s):
        if not s:
            return 0
        left=0
        n=len(s)
        lookup=set()
        max_len=0
        cur_len=0
        for i in range(n):
            cur_len+=1
            while s[i] in lookup:
                lookup.remove(s[left])
                left+=1
                cur_len-=1
            max_len=max(max_len,cur_len)
            lookup.add(s[i])
        return max_len


if __name__ == "__main__":
    s = solution()
    str="abcabcbb"
    print(s.Qili(str))
