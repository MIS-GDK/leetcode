# 106. 从中序与后序遍历序列构造二叉树
# 根据一棵树的中序遍历与后序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。
# 例如，给出

# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]

# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        root = postorder[-1]
        res = TreeNode(root)
        i = inorder.index(root)
        res.left = self.buildTree(inorder[:i], postorder[:i])
        res.right = self.buildTree(inorder[i + 1 :], postorder[i : len(postorder) - 1])

        return res