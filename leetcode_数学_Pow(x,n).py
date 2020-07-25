"""
快速幂
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        judge = True
        if n < 0:
            n = -n
            judge = False
        final = 1
        while n>0:
            if n%2 == 0:
                x *=x
                n //= 2
            final *= x
            n -= 1
        return final if judge else 1/final


class Solution:
    def myPow(self, x,n):
        if n < 0 :
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return x * self.myPow(x*x, n//2)



