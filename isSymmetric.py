# 101. 对称二叉树

# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3


# 进阶：

# 你可以运用递归和迭代两种方法解决这个问题吗？
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/symmetric-tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.ismirror(root.left, root.right)

    def ismirror(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        if root1.val == root2.val:
            return self.ismirror(root1.left, root2.right) and self.ismirror(
                root1.right, root2.left
            )
        else:
            return False
