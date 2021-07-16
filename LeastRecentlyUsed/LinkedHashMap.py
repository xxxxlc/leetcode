
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None

class DoubleList(object):
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
    
    def addLast(self, x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x

        self.size += 1
    
    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first
    
    def get_size(self):
        return self.size

class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.map = dict()
        self.cache = DoubleList()
    
    # 将某个key提升到最近使用
    def makeRecently(self, key):
        x = self.map.get(key)
        self.cache.remove(x)
        self.cache.addLast(x)

    # 添加最近使用的元素
    def addRecently(self, key, val):
        x = Node(key, val)
        self.cache.addLast(x)
        self.map[key] = x

    def deleteKey(self, key):
        x = self.map.get(key)
        self.cache.remove(x)
        self.map.pop(key)
    
    # 删除最久未使用的元素
    def removeLeastRecently(self):
        deleteNode = self.cache.removeFirst()
        deleteKey = deleteNode.key
        self.map.pop(deleteKey)

    # 将该数据提升为最近使用
    def get(self, key):
        if key not in self.map.keys():
            return -1
        
        self.makeRecently(key)
        return self.map[key].val
    
    def put(self, key, val):
        if key in self.map.keys():
            self.deleteKey(key)
            self.addRecently(key, val)
            return
        
        else:
            if self.cap == self.cache.get_size():
                self.removeLeastRecently()
            
            self.addRecently(key, val)
        

if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1); 
    lRUCache.put(2, 2); 
    print(lRUCache.get(1));    
    lRUCache.put(3, 3); 

import collections
class LRUCache1(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

