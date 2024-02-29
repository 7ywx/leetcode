#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (77.36%)
# Likes:    1783
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树 root ，返回其最大深度。
#
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
#
#
#
# 示例 1：
#
#
#
#
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
#
#
# 示例 2：
#
#
# 输入：root = [1,null,2]
# 输出：2
#
#
#
#
# 提示：
#
#
# 树中节点的数量在 [0, 10^4] 区间内。
# -100 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)

        # return max(left_depth, right_depth) + 1

        depth, left_depth = 0, 0
        if not root:
            return depth
        else:
            depth = 1
        if root.left:
            depth += self.maxDepth(root.left)
            left_depth = depth
            depth = 1
        if root.right:
            depth += self.maxDepth(root.right)
        return max(left_depth, depth)
# @lc code=end
