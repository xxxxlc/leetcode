# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入



from timeit import repeat


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.display(s, 0, len(s))

    
    def display(self, s, start, end):
        ans = ''
        i = start

        while(i < end):
            if s[i].isdigit():

                digit = ''
                while(s[i].isdigit()):
                    digit += s[i]
                    i += 1

                repeat = i
                stack = [s[repeat]]
                while(stack):
                    repeat += 1
                    if s[repeat] == "]":
                        stack.pop()
                    elif s[repeat] == "[":
                        stack.append(s[repeat])

                ans += self.display(s, i + 1, repeat) * int(digit)
                i = repeat + 1
            else:
                ans += s[i]
                i += 1
        return ans



s = "2[abc]3[cd]ef"

a = Solution()
print(a.decodeString(s))