#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# https://leetcode.cn/problems/path-sum/description/
#
# algorithms
# Easy (54.66%)
# Likes:    1390
# Dislikes: 0
# Total Accepted:    728.6K
# Total Submissions: 1.3M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点
# 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
#
# 叶子节点 是指没有子节点的节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
# 解释：等于目标和的根节点到叶节点路径如上图所示。
#
#
# 示例 2：
#
#
# 输入：root = [1,2,3], targetSum = 5
# 输出：false
# 解释：树中存在两条根节点到叶子节点的路径：
# (1 --> 2): 和为 3
# (1 --> 3): 和为 4
# 不存在 sum = 5 的根节点到叶子节点的路径。
#
# 示例 3：
#
#
# 输入：root = [], targetSum = 0
# 输出：false
# 解释：由于树是空的，所以不存在根节点到叶子节点的路径。
#
#
#
#
# 提示：
#
#
# 树中节点的数目在范围 [0, 5000] 内
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # bfs 加法思维
        if not root: return False
        queue = [root]
        queue_sum = [root.val]
        while queue:
            node = queue.pop(0)
            q_sum = queue_sum.pop(0)
            if not node.left and not node.right and q_sum == targetSum:
                return True
            if node.left:
                queue.append(node.left)
                queue_sum.append(q_sum + node.left.val)
            if node.right:
                queue.append(node.right)
                queue_sum.append(q_sum + node.right.val)
        return False

        # dfs 递归 减法思维
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
# @lc code=end
