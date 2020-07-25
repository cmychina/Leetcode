# -*- coding:utf-8 -*-
class Solution:
    """
    可以基于数学证明，按3分割最好
    a1a2...an<=((a1+a2+...an)/n)^n
    a1a2...an<=(k/n)^n
    loga1a2...an<=nlog(k/n)
    导数为logk-logn-1=0 ->k/n=e->n=k/e
    所以按e切分最好
    """
    def cutRope(self, number):
        res = 1
        while number > 4:
            res *= 3
            number -= 3
        res *= number
        return res
