# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。

class Solution(object):
    tree_dict = dict()
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        if label in self.tree_dict.keys():
            return self.tree_dict[label]
        
        elif label == 1:
            self.tree_dict[label] = [1]
            return self.tree_dict[label]
        
        else:
            s = 1
            i = 1
            
            while(s < label):
                i = i * 2
                s += i
            
            num1 = i - (s - label)
            num2 = (num1 - 1) // 2
            pre = self.pathInZigZagTree(label - num1 - num2)
            self.tree_dict[label] = pre[:] + [label]

            return self.tree_dict[label]



a = Solution()
print(a.pathInZigZagTree(14))
