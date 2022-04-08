# 给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。

# 「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。


class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        ans = 0
        for i in arr1:
            isdis = False
            for j in arr2:
                if abs(i - j) <= d:
                    isdis = True
            if not isdis:
                ans += 1
        
        return ans


arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2

a = Solution()
print(a.findTheDistanceValue(arr1, arr2, d))