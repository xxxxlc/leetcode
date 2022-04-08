# 给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。

# 请你找到这个数组里第 k 个缺失的正整数。


class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        c = 1
        s = []
        i = 0
        while (i < len(arr)):
            if arr[i] != i + c:
                s.append(i + c)
                c += 1
                if len(s) == k:
                    return s[-1]
                continue
            i += 1
        
        return arr[-1] + k - len(s)


arr = [5,6,7,8,9]
k = 9
a = Solution()

print(a.findKthPositive(arr, k))
