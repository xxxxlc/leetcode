# 给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。

# 更正式地，检查是否存在两个下标 i 和 j 满足：

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] != 0 and arr[j] != 0 and (arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]):
                    return True
                if arr[i] == 0 and arr[j] == 0:
                    return True
        
        return False

arr = [-2,0,10,-19,4,6,-8]
a = Solution()
print(a.checkIfExist(arr))