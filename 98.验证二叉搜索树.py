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
    #TODO 这三个
    # 后序
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple:
            if node is None:
                return inf, -inf
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            x = node.val
            # 也可以在递归完左子树之后立刻判断，如果发现不是二叉搜索树，就不用递归右子树了
            if x <= l_max or x >= r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)
        return dfs(root)[1] != inf

    # 中序
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left) or root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)

    # 前序
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True
        x = root.val
        return left < x < right and \
                self.isValidBST(root.left, left, x) and \
                self.isValidBST(root.right, x, right)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 二叉树的中序遍历（迭代）
        # res = [float('-inf')]  # 存储结果的列表
        res = float('-inf')
        stack = []  # 存储节点的栈
        while root or stack:  # 当根节点或栈不为空时
            while root:  # 当根节点不为空时
                stack.append(root)  # 将根节点压入栈中
                root = root.left  # 将根节点指向左子节点
            root = stack.pop()  # 弹出栈顶节点
            if root.val > res:
                res = root.val  # 将节点的值添加到结果列表中
            else:
                return False
            root = root.right  # 将根节点指向右子节点
        return True  # 返回结果列表
# @lc code=end
