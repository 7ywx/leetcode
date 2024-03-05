#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (45.42%)
# Likes:    2177
# Dislikes: 0
# Total Accepted:    382.5K
# Total Submissions: 842.1K
# Testcase Example:  '[1,2,3]'
#
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个
# 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
#
# 示例 2：
#
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#
#
#
#
# 提示：
#
#
# 树中节点数目范围是 [1, 3 * 10^4]
# -1000 <= Node.val <= 1000
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
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 标签 递归 最值 self.res 要在外面定义
        self.node = root
        self.res = float('-inf')
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            # self.res = float('-inf')
            cur = root.val
            left = dfs(root.left)
            right = dfs(root.right)

            if left > right:
                if left > 0:
                    cur += left
                if right > 0:
                    if cur + right > self.res:
                        self.res = cur + right
            else:
                if right > 0:
                    cur += right
                if cur + left > self.res:
                    self.res = cur + left

            if cur > self.res:
                self.res = cur
            return cur
        dfs(root)
        return self.res
# @lc code=end
# 手动创建二叉树
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(-2)
root.left.left.left = TreeNode(-1)

root1 = TreeNode(-10)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

solution = Solution()
res = solution.maxPathSum(root1)
