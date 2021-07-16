# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        self.visited = set()
        q = ['0000']
        res = 0
        while(q):
            size = len(q)
            for i in range(0, size):
                cur = q.pop(0)
                if cur in deadends:
                    continue
                if cur == target:
                    return res
                
                for j in range(0, 4):
                    up = self.plusone(cur, j)
                    if up not in self.visited:
                        self.visited.add(up)
                        q.append(up)
                    
                    down = self.minusone(cur,j)
                    if down not in self.visited:
                        self.visited.add(down)
                        q.append(down)
            res += 1
        

        return -1


    
    def plusone(self, s, j):
        ch = list(s)
        if ch[j] == '9':
            ch[j] == '0'
        else:
            ch[j] = chr(ord(ch[j]) + 1)
        
        return "".join(ch)
    
    def minusone(self, s, j):
        ch = list(s)
        if ch[j] == '0':
            ch[j] = '9'
        else:
            ch[j] = chr(ord(ch[j]) - 1)
        
        return "".join(ch)



a = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(a.openLock(deadends, target))