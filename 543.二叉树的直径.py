#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode.cn/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (59.66%)
# Likes:    1491
# Dislikes: 0
# Total Accepted:    385.2K
# Total Submissions: 645.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你一棵二叉树的根节点，返回该树的 直径 。
#
# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
#
# 两节点之间路径的 长度 由它们之间边数表示。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4,5]
# 输出：3
# 解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
#
#
# 示例 2：
#
#
# 输入：root = [1,2]
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [1, 10^4] 内
# -100 <= Node.val <= 100
#
#
#
from typing import Optional, List
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
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         # 二叉树的直径，就是左右子树的最大深度之和
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node = L + R + 1 (1是那个根) 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
# @lc code=end
def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        current_node = queue.pop(0)

        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)

        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)

        i += 1

    return root

# 用给定的节点列表构建二叉树
nodes_list = [1, 2, 3, 4, 5]
root = build_tree(nodes_list)

solution = Solution()
solution.diameterOfBinaryTree(root)
