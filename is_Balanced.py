# 110. 平衡二叉树

# 一棵高度平衡二叉树定义为：
#     一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 自底向上的递归
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode):
            if not root:
                return 0
            leftChild = height(root.left)
            rightChild = height(root.right)

            if leftChild == -1 or rightChild == -1 or abs(leftChild - rightChild) > 1:
                return -1
            else:
                return max(leftChild, rightChild) + 1

        return height(root) >= 0
