#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode.cn/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (37.62%)
# Likes:    2282
# Dislikes: 0
# Total Accepted:    852.4K
# Total Submissions: 2.3M
# Testcase Example:  '[2,1,3]'
#
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
#
#
# 示例 1：
#
#
# 输入：root = [2,1,3]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#
#
#
#
# 提示：
#
#
# 树中节点数目范围在[1, 10^4] 内
# -2^31 <= Node.val <= 2^31 - 1
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = [float('-inf')]  # 存储结果的列表
        stack = []  # 存储节点的栈
        while root or stack:  # 当根节点或栈不为空时
            while root:  # 当根节点不为空时
                stack.append(root)  # 将根节点压入栈中
                root = root.left  # 将根节点指向左子节点
            root = stack.pop()  # 弹出栈顶节点
            if root.val > res[-1]:
                res.append(root.val)  # 将节点的值添加到结果列表中
            else:
                return False
            root = root.right  # 将根节点指向右子节点
        return True  # 返回结果列表
# @lc code=end
