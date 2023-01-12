# 给你一个字符串 s ，它包含一些括号对，每个括号中包含一个 非空 的键。

# 比方说，字符串 "(name)is(age)yearsold" 中，有 两个 括号对，分别包含键 "name" 和 "age" 。
# 你知道许多键对应的值，这些关系由二维字符串数组 knowledge 表示，其中 knowledge[i] = [keyi, valuei] ，表示键 keyi 对应的值为 valuei 。

# 你需要替换 所有 的括号对。当你替换一个括号对，且它包含的键为 keyi 时，你需要：

# 将 keyi 和括号用对应的值 valuei 替换。
# 如果从 knowledge 中无法得知某个键对应的值，你需要将 keyi 和括号用问号 "?" 替换（不需要引号）。
# knowledge 中每个键最多只会出现一次。s 中不会有嵌套的括号。

# 请你返回替换 所有 括号对后的结果字符串。

class Solution:
    def evaluate(self, s: str, knowledge: list) -> str:
        
        d = {}

        for key, val in knowledge:
            d[key] = val


        ans = ''

        i = 0
        n = len(s)
        while (i < n):
            if s[i] == '(':
                j = i + 1
                while(s[j] != ')'):
                    j += 1
                
                key = s[i+1:j]

                if key not in d:
                    ans += '?'
                else:
                    ans += d[key]
                
                i = j + 1

            else:
                ans += s[i]
                i += 1


        return ans



s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]

a = Solution()
print(a.evaluate(s, knowledge))