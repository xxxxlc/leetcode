# 给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。

# 请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        n = len(salary) - 2

        return (sum(salary) - max(salary) - min(salary)) / n

salary = [4000,3000,1000,2000]

a = Solution()
print(a.average(salary))