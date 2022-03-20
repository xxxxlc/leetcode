# 这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr[i]。

# 请你判断自己是否能够跳到对应元素值为 0 的 任一 下标处。

# 注意，不管是什么情况下，你都无法跳到数组之外。



class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if arr[start] == 0:
            return True
        n = len(arr)
        used = {start}
        q = collections.deque([start])

        while len(q) > 0:
            u = q.popleft()
            for v in [u + arr[u], u - arr[u]]:
                if 0 <= v < n and v not in used:
                    if arr[v] == 0:
                        return True
                    q.append(v)
                    used.add(v)
        
        return False
    

arr = [4,2,3,0,3,1,2]
start = 5

a = Solution()
print(a.canReach(arr, start))
