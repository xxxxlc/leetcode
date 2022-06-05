# 给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。

# 如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。

# 请你返回排序后的数组。


from functools import cmp_to_key


class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # for i in arr:
        #     print(bin(i))
        #     print(bin(i).count('1'))
        

        arr = sorted(arr, key=lambda x:(bin(x).count('1'), x))

        return arr
    


arr = [1024,512,256,128,64,32,16,8,4,2,1]

a = Solution()
print(a.sortByBits(arr))