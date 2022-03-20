# 有两个水壶，容量分别为 jug1Capacity 和 jug2Capacity 升。水的供应是无限的。确定是否有可能使用这两个壶准确得到 targetCapacity 升。

# 如果可以得到 targetCapacity 升水，最后请用以上水壶中的一或两个来盛放取得的 targetCapacity 升水。

# 你可以：

# 装满任意一个水壶
# 清空任意一个水壶
# 从一个水壶向另外一个水壶倒水，直到装满或者倒空

class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """

        stack = [(0, 0)]
        seen = set()

        while(stack):
            remain_x, remain_y = stack.pop(0)

            if remain_x == targetCapacity or remain_y == targetCapacity or remain_y + remain_x == targetCapacity:
                return True
            
            if (remain_x, remain_y) in seen:
                continue
            
            seen.add((remain_x, remain_y))

            stack.append((jug1Capacity, remain_y))
            stack.append((remain_x, jug2Capacity))
            stack.append((0, remain_y))
            stack.append((remain_x, 0))
            stack.append((remain_x - min(remain_x, jug2Capacity - remain_y), remain_y + min(remain_x, jug2Capacity - remain_y)))
            stack.append((remain_x + min(remain_y, jug1Capacity - remain_x), remain_y - min(remain_y, jug1Capacity - remain_x)))
        return False

jug1Capacity = 3
jug2Capacity = 5
targetCapacity = 4

a = Solution()
print(a.canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))