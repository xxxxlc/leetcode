# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。

# 例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。

# 分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。

# 我们称所有包含大于或等于三个连续字符的分组为 较大分组 。

# 找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。

class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        start_index = 0
        end_index = 0
        result = []
        j = 0
        while(j < len(s) - 1):
            if s[j] == s[j+1]:
                end_index = end_index + 1
                j = j + 1
                if j == len(s) - 1:
                    if end_index - start_index > 1:
                        result.append([start_index, end_index])
                continue
            else:
                if end_index - start_index > 1:
                    result.append([start_index, end_index])
                j = j + 1
                start_index = j
                end_index = j
        return result






a = Solution()
s =  "aaa"
print(a.largeGroupPositions(s))