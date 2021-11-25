# 请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)

        queue = []

        for i in range(0, len(temperatures)):
            if not queue:
                queue.append([temperatures[i], i])
                continue

            while(queue):
                if queue[-1][0] < temperatures[i]:
                    pre = queue.pop(-1)
                    ans[pre[1]] = i - pre[1]
                else:
                    break

            queue.append([temperatures[i], i])
        
        return ans




temperatures = [73,74,75,71,69,72,76,73]
a = Solution()
print(a.dailyTemperatures(temperatures))