# 给你一个下标从 0 开始的字符串 s ，该字符串仅由小写英文字母组成，s 中的每个字母都 恰好 出现 两次 。另给你一个下标从 0 开始、长度为 26 的的整数数组 distance 。

# 字母表中的每个字母按从 0 到 25 依次编号（即，'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25）。

# 在一个 匀整 字符串中，第 i 个字母的两次出现之间的字母数量是 distance[i] 。如果第 i 个字母没有在 s 中出现，那么 distance[i] 可以 忽略 。

# 如果 s 是一个 匀整 字符串，返回 true ；否则，返回 false 。

class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        d = dict()

        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)
        
        for i in range(len(distance)):
            c = chr(97 + i)
            if c not in d.keys():
                continue
            else:
                if abs(d[c][0] - d[c][1]) - 1 != distance[i]:
                    return False
        
        return True


s = "aa"
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

a = Solution()
print(a.checkDistances(s, distance))