# 给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：

# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# 注意 ^ 表示 按位异或（bitwise-xor）运算。

# 可以证明答案是 唯一 的。

class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(pref)

        for i in range(len(pref)):
            if i == 0:
                ans[i] = pref[i]
            else:
                ans[i] = pref[i - 1] ^ pref[i]
        return ans

pref = [5,2,0,3,1]

a = Solution()
print(a.findArray(pref))