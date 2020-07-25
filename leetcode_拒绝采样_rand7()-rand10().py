import random
def rand7():
    return random.choice(0,7)

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            num = col + (row - 1) * 7
            if num <= 40:
                break
        return 1 + (num - 1) % 10 # 1-10