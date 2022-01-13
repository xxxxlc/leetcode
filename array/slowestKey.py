# 请返回按键 持续时间最长 的键，如果有多个这样的键，则返回 按字母顺序排列最大 的那个键。

class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        maxtime = 0
        keys = None
        for i in range(0, len(releaseTimes)):
            if i == 0:
                pressedtime = releaseTimes[i] - 0
            else:
                pressedtime = releaseTimes[i] - releaseTimes[i - 1]

            if pressedtime > maxtime:
                maxtime = pressedtime
                keys = keysPressed[i]
            elif pressedtime == maxtime:
                if ord(keysPressed[i]) > ord(keys):
                    keys = keysPressed[i]
        
        return keys
        

a = Solution()
releaseTimes = [9,29,49,50]
keysPressed = "cbcd"
print(a.slowestKey(releaseTimes, keysPressed))