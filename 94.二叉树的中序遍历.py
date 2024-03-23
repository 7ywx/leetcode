#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (76.58%)
# Likes:    2043
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 1.8M
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#
#
# 示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
#
#
#
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #TODO Morris 中序遍历
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        #标签 迭代
        res = []  # 存储结果的列表
        stack = []  # 存储节点的栈
        while root or stack:  # 当根节点或栈不为空时
            while root:  # 当根节点不为空时
                stack.append(root)  # 将根节点压入栈中
                root = root.left  # 将根节点指向左子节点
            root = stack.pop()  # 弹出栈顶节点
            res.append(root.val)  # 将节点的值添加到结果列表中
            root = root.right  # 将根节点指向右子节点
        return res  # 返回结果列表

        # #标签 颜色标记法
        # """
        # - 使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
        # - 如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
        # - 如果遇到的节点为灰色，则将节点的值输出。
        # """
        # WHITE, GRAY = 0, 1
        # res = []
        # stack = [(WHITE, root)]
        # while stack:
        #     color, node = stack.pop()
        #     if node is None: continue
        #     if color == WHITE:
        #         stack.append((WHITE, node.right))
        #         stack.append((GRAY, node))
        #         stack.append((WHITE, node.left))
        #     else:
        #         res.append(node.val)
        # return res

        # #标签 递归
        # res = []  # 存储中序遍历结果的列表
        # if not root:  # 如果根节点为空，则返回空列表
        #     return res
        # res += (self.inorderTraversal(root.left))  # or res.extend() 递归调用左子树的中序遍历，并将结果添加到res列表中
        # res.append(root.val)  # 将当前节点的值添加到res列表中
        # res += (self.inorderTraversal(root.right))  # 递归调用右子树的中序遍历，并将结果添加到res列表中
        # return res  # 返回中序遍历结果的列表
# @lc code=end
solution = Solution()
root = TreeNode(val=1, left=None, right=TreeNode(val=2,left=TreeNode(3),right=None))
print(solution.inorderTraversal(root))
