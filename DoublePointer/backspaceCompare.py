# 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

# 注意：如果对空文本输入退格字符，文本继续为空。


from inspect import stack


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []


        j = 0
        while (j < len(s)):
            if s[j] == "#":
                if stack1:
                    stack1.pop()
                j += 1
                continue
            stack1.append(s[j])
            j += 1

        j = 0
        while (j < len(t)):
            if t[j] == "#":
                if stack2:
                    stack2.pop()
                j += 1
                continue
            stack2.append(t[j])
            j += 1
        
        if len(stack1) != len(stack2):
            return False

        for i in range(len(stack1)):
            if stack1[i] != stack2[i]:
                return False
        
        return True



        

s = "y#fo##f"
t = "y#f#o##f"

a = Solution()
print(a.backspaceCompare(s, t))