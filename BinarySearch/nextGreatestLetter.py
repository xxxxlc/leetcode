# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

# 在比较时，字母是依序循环出现的。举个例子：

# 如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[-1] <= target:
            return letters[0]

        left = 0
        right = len(letters) - 1

        while (left < right):
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return letters[left]

letters = ["c", "f", "j"]
target = "j"

a = Solution()
print(a.nextGreatestLetter(letters, target))