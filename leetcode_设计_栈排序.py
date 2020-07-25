"""
栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。
该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。
"""


class SortedStack:
    def __init__(self):
        self.data = []
        self.Len = 0  # 当前元素的个数

    def push(self, val: int) -> None:
        self.data.append(val)  # 往小根堆里加数据
        self.Len += 1
        if self.Len >= 2:  # 小根堆的元素数大于 2 时，需要对小根堆进行调整
            self.adjustUp(self.Len - 1)  # 元素向上调整

    def adjustUp(self, child):
        temp = self.data[child]
        parent = (child - 1) // 2  # 当前元素的父节点元素的idx
        while parent >= 0:
            if self.data[parent] > temp:
                self.data[child] = self.data[parent]
            else:
                break
            child = parent
            parent = (child - 1) // 2
        self.data[child] = temp

    def pop(self) -> None:
        if self.data == []:
            return
            # 将当前最小元素与最后一个元素交换，最后一个元素pop
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        self.Len -= 1
        self.adjustDown(0)  # 此时将刚交换放在第一个位置的元素向下调整到合适的位置
        return self.data.pop()

    def adjustDown(self, parent):
        temp = self.data[parent]
        child = 2 * parent + 1
        while child < self.Len:
            # 找到最小的孩子
            if child + 1 < self.Len and self.data[child + 1] < self.data[child]:
                child += 1
            if self.data[child] < temp:
                self.data[parent] = self.data[child]
            else:
                break
            parent = child
            child = 2 * parent + 1
        self.data[parent] = temp

    def peek(self) -> int:  # 查看当前最小的元素
        if self.Len == 0:
            return -1
        return self.data[0]

    def isEmpty(self) -> bool:  # is empty ?
        return self.Len == 0


class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.swim(len(self.stack) - 1)

    def swap(self,i,j):
        self.stack[i],self.stack[j]=self.stack[j],self.stack[i]

    def pop(self) -> None:
        if not self.stack:
            return
        self.swap(0,-1)
        self.stack.pop()
        self.sink(0)

    def peek(self) -> int:
        return self.stack and self.stack[0] or -1

    def isEmpty(self) -> bool:
        return not self.stack

    def sink(self, j):
        n = len(self.stack)
        while 2 * j + 1 < n:
            left = 2 * j + 1
            right= 2 * j + 2
            if j < n - 1 and self.stack[left] > self.stack[right]:
                left=right
            if self.stack[j] <= self.stack[left]:
                break
            self.swap(j,left)
            j = left

    def swim(self, j):
        parent=(j - 1) // 2
        if j>0 and self.stack[j] < self.stack[parent]:
            self.swap(j,parent)
            self.swim(parent)


class SortedStack:

    def __init__(self):
        self.data = []
        self.helper = []

    def push(self, val: int) -> None:

        if not self.data: # 如果 data 为空，直接将元素添加到data中
            self.data.append(val)
        else:
            # 如果 data 顶的元素比val小，将 data 中比 val 小的元素倒到 helper 中
            #然后将 val 放入 data 顶
            if self.data[-1] < val:
                while self.data and self.data[-1] < val:
                    self.helper.append(self.data.pop(-1))
                self.data.append(val)
            # 如果 data 顶的元素等于 val，直接将 val 放在 data 顶
            elif self.data[-1] == val:
                self.data.append(val)
            else:
                # 此时的情况为：val < sel.data[-1]，需要把 helper 中比 val 大的元素倒到data顶去
                # case 1, 如果helper 为空，或者 val 大于等于 helper 顶的元素
                # 直接将val 放到 data 顶
                if not self.helper or self.helper[-1] <= val:
                    self.data.append(val)
                else:
                    # case 2, val 小于 helper 的栈顶元素，则把小于 val 的元素倒回 data 中
                    # 然后把 val 放在 data 栈顶
                    while self.helper and val < self.helper[-1]:
                        self.data.append(self.helper.pop())
                    self.data.append(val)

    def pop(self) -> None:
        if not self.data:
            return -1
        # 由于 helper 中会放有较小的元素，
        # 首先检查 helper 是否有元素，有的话将其倒入 data 中
        # pop data 顶的元素（当前最小值）
        while self.helper:
            self.data.append(self.helper.pop())
        return self.data.pop()

    def peek(self) -> int:
        if not self.data:
            return -1
        while self.helper:
            self.data.append(self.helper.pop())
        return self.data[-1]

    def isEmpty(self) -> bool:
        return self.data == []
