# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

# 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对

import Bintree
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ''

        left = self.tree2str(t.left)
        right = self.tree2str(t.right)

        if left == '' and right == '':
            return str(t.val)
        elif left != '' and right == '':
            return str(t.val) + '(' + left + ')'

        return str(t.val) + '(' + left + ')' + '(' + right + ')'


root = [1,2,3,4]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.tree2str(tree.root))