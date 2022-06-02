# 请你设计一个可以解释字符串 command 的 Goal 解析器 。command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成。Goal 解析器会将 "G" 解释为字符串 "G"、"()" 解释为字符串 "o" ，"(al)" 解释为字符串 "al" 。然后，按原顺序将经解释得到的字符串连接成一个字符串。

# 给你字符串 command ，返回 Goal 解析器 对 command 的解释结果。

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        stack = ""
        i = 0
        ans = ""
        while (i < len(command)):
            if command[i] == "(":
                stack += command[i]
            elif command[i] == ")":
                stack += command[i]
                if stack == "()":
                    ans += "o"
                elif stack == "(al)":
                    ans += "al"
                stack = ""
            else:
                if len(stack) == 0:
                    ans += command[i]
                else:
                    stack += command[i]
            i += 1
        return ans

command = "G()(al)"

a = Solution()
print(a.interpret(command))
