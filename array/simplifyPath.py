# 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。

# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。

# 请注意，返回的 规范路径 必须遵循下述格式：

# 始终以斜杠 '/' 开头。
# 两个目录名之间必须只有一个斜杠 '/' 。
# 最后一个目录名（如果存在）不能 以 '/' 结尾。
# 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
# 返回简化后得到的 规范路径 。

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = ["/"]
        i = 0
        pointnum = 0

        for i in range(len(path) + 1):
            if i < len(path) and path[i] == "." and stack[-1] == "/":
                pointnum += 1
            elif i == len(path) or path[i] == "/":
                if pointnum > 2:
                    stack.extend("." for _ in range(pointnum))
                elif pointnum == 2:
                    if len(stack) > 1:
                        if stack[-1] == "/":
                            stack.pop()
                        while (stack.pop() != "/" and len(stack) > 1):
                            pass
                pointnum = 0
                if stack[-1] != "/":
                    stack.append("/")
            else:
                stack.extend("." for _ in range(pointnum))
                stack.append(path[i])
                pointnum = 0
        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        return "".join(stack)

        # while (i < len(path)):
        #     if path[i] == ".":
        #         pointnum += 1
        #         if i == len(path) - 1:
        #             if pointnum > 2:
        #                 stack.extend("." for _ in range(pointnum))
        #             elif pointnum == 2:
        #                 if len(stack) > 1:
        #                     if stack[-1] == "/":
        #                         stack.pop()
        #                     while (stack.pop() != "/" and len(stack) > 1):
        #                         pass
        #     else:
        #         if pointnum > 2:
        #             stack.extend("." for _ in range(pointnum))
        #         elif pointnum == 2:
        #             if len(stack) > 1:
        #                 if stack[-1] == "/":
        #                     stack.pop()
        #                 while (stack.pop() != "/" and len(stack) > 1):
        #                     pass
        #         pointnum = 0

        #         if path[i] == "/" and stack[-1] != "/" or path[i] != "/":
        #              stack.append(path[i])
        #     i += 1
        # if len(stack) > 1 and stack[-1] == "/":
        #     stack.pop()
        # return "".join(stack)



path = "/hello../world"

a = Solution()
print(a.simplifyPath(path))