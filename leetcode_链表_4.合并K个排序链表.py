"""
优先级队列
优先级队列最重要的就是要实现快速得到队列中优先级最高的元素
因此，优先队列有一定的顺序特点，这是一种弱序，即队列头部的那个元素是优先级最高的

heap
1.使用heap.heapify(list)转换列表成为堆结构
2.heapq.merge(*iterables),用于合并多个排序后的序列成一个排序后的序列，返回排序后的值的迭代器。
3.heapq.heappop() 函数弹出堆中最小值
4.heapq.heaprepalce() 删除堆中最小元素并加入一个元素
5.如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数
6.实现heap堆排序算法
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


heap = [] #创建了一个空堆
heappush(heap,item) #往堆中插入一条新的值
item = heappop(heap) #从堆中弹出最小值
item = heap[0] #查看堆中最小值，不弹出
heapify(x) #以线性时间讲一个列表转化为堆

"""
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]

#本题暴力解法是N个数放在一个数组再排序，复杂度NlogN
#由于每个链表都是有序的，可以考虑维护k个指针，每次选出最小的，可以通过最小堆实现，复杂度Nlogk
#先把每个链表的头结点放进一个最小堆，然后依次连接，每次连接 重新把链表值如堆更新
from linklist import ListNode
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return
        n=len(lists)
        return self.merge(lists,0,n-1)

    def merge(self,lists,left,right):
        if left==right:
            return lists[left]
        mid=left+(right-left)//2
        l1=self.merge(lists,left,mid)
        l2=self.merge(lists,mid+1,right)
        return self.mergeTwoLists(l1,l2)

    def mergeTwoLists(self, l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
#O(knlog(k))
# import heapq
# a=[2,5,6,8,3,9]
# heapq.heapify(a)
# print([heapq.heappop(a) for _ in range(len(a))])
#
# num1 = [32, 3, 5, 34, 54, 23, 132]
# num2 = [23, 2, 12, 656, 324, 23, 54]
# num1 = sorted(num1)
# num2 = sorted(num2)
#
# res = heapq.merge(num1, num2)
# print(list(res))