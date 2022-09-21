class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        input = input.split("\n")
        res = 0
        nums = []

        for i in input:
            file = i.split("\t")[-1]
            tNum = len(i.split("\t")) - 1
            if len(nums) > tNum:
                nums[tNum] = file
            else:
                nums.append(file)
            if "." in i:
                temp_res = len("".join(nums[:tNum+1])) + tNum
                res = max(temp_res, res)
        
        return res





input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

a = Solution()
print(a.lengthLongestPath(input))