"""
关键点是顶一个一个move_to_tail的方法
"""
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到末尾，所以定义一个方法
    def move_node_to_tail(self, key):
            # 先将哈希表key指向的节点拎出来，为了简洁起名node
            #      hashmap[key]                               hashmap[key]
            #           |                                          |
            #           V              -->                         V
            # prev <-> node <-> next         pre <-> next   ...   node
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            # 之后将node插入到尾节点前
            #                 hashmap[key]                 hashmap[key]
            #                      |                            |
            #                      V        -->                 V
            # prev <-> tail  ...  node                prev <-> node <-> tail
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到末尾（变成最新访问的）
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到末尾
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                # 去掉哈希表对应项
                self.hashmap.pop(self.head.next.key)
                # 去掉最久没有被访问过的节点，即头节点之后的节点
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 如果不在的话就插入到尾节点前
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new

class LRUCache:
    """
    双向链表的开头表示最近访问的节点，最末尾表示最久未使用的节点。
    get的时候，先通过字典获取到节点，执行delete然后执行insert，相当于把节点移到了双向链表的开头。
    put的时候，如果键存在，先覆盖node的值，依然执行delete然后执行insert，相当于把节点移到了双向链表的开头。
    如果键不存在，需要插入新节点，这时如果容量已满，先删除最后一个节点，没满就不删除，然后执行insert方法，tail.prev就是最后一个节点。

    """
    def __init__(self, capacity: int):
        self.dic={}
        self.head=ListNode(None,None)
        self.tail=ListNode(None,None)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity

    def get(self, key: int) -> int:
        if not key in self.dic:
            return -1
        node=self.dic[key]
        self.delete(node)
        self.insert(node)
        return node.val

    #将node插入到头结点后
    def insert(self,node):
        node.next,node.prev=self.head.next,self.head
        temp=self.head.next
        self.head.next=node
        temp.prev=node

    def delete(self,node):
        node.prev.next,node.next.prev=node.next,node.prev

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node=self.dic[key]
            node.val=value
            self.delete(node)
            self.insert(node)
            return
        if len(self.dic)==self.capacity:
            node=self.tail.prev
            self.delete(node)
            del self.dic[node.key]
        node=ListNode(key,value)
        self.dic[key]=node
        self.insert(node)

