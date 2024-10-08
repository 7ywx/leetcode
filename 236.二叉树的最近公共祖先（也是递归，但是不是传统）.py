#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (70.68%)
# Likes:    2621
# Dislikes: 0
# Total Accepted:    666.1K
# Total Submissions: 942K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
#
#
# 示例 1：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
#
#
# 示例 2：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
#
#
# 示例 3：
#
#
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [2, 10^5] 内。
# -10^9
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。
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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 标签 递归

        # 如果当前节点为空，返回 None
        if not root:
            return None

        # 如果当前节点是 p 或 q 中的一个，直接返回当前节点
        if root == p or root == q:
            return root

        # 递归查找左右子树
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右子树都找到了节点，说明当前节点就是最近公共祖先
        if left and right:
            return root

        # 如果只有一个子树找到了节点，则说明该节点是公共祖先
        # 如果两个子树都没找到节点，则返回 None
        return left if left else right
# @lc code=end

# 示例用法
# 构建示例二叉树
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# 创建解决方案实例
solution = Solution()

# 指向两个节点的指针
p = root.left.left
q = root.left.right.left

# 找到最近公共祖先
result = solution.lowestCommonAncestor(root, p, q)
print(result.val)
