import random
import math
#极坐标
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        rou = self.radius * math.sqrt(random.random())
        theta = random.random() * math.pi * 2
        x = rou * math.cos(theta) + self.x_center
        y = rou * math.sin(theta) + self.y_center
        return [x, y]
#拒绝法采样
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        while 1:
            x = random.uniform(-self.radius, self.radius)
            y = random.uniform(-self.radius, self.radius)
            if math.sqrt(x**2+y**2)<=self.radius:
                return [self.x_center+x, self.y_center+y]