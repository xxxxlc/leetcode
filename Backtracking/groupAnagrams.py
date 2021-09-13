# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母都恰好只用一次


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []

        map = dict()

        for c in strs:
            s = list(c)
            s.sort()
            s = "".join(s)
            if s not in map.keys():
                map[s] = []
                map[s].append(c)
            else:
                map[s].append(c)
        
        for key, values in map.items():
            ans.append(values)

        return ans


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

a = Solution()
print(a.groupAnagrams(strs))