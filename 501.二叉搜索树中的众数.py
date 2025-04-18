#
# @lc app=leetcode.cn id=501 lang=python3
# @lcpr version=30104
#
# [501] 二叉搜索树中的众数
#
# https://leetcode.cn/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (55.67%)
# Likes:    795
# Dislikes: 0
# Total Accepted:    252.2K
# Total Submissions: 449K
# Testcase Example:  '[1,null,2,2]'
#
# 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
#
# 如果树中有不止一个众数，可以按 任意顺序 返回。
#
# 假定 BST 满足如下定义：
#
#
# 结点左子树中所含节点的值 小于等于 当前节点的值
# 结点右子树中所含节点的值 大于等于 当前节点的值
# 左子树和右子树都是二叉搜索树
#
#
#
#
# 示例 1：
#
# 输入：root = [1,null,2,2]
# 输出：[2]
#
#
# 示例 2：
#
# 输入：root = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 树中节点的数目在范围 [1, 10^4] 内
# -10^5 <= Node.val <= 10^5
#
#
#
#
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.counter = defaultdict(int)
        self.max_time = 0

        def in_order(root):
            if not root:
                return

            in_order(root.left)
            self.counter[root.val] += 1
            if self.counter[root.val] > self.max_time:
                self.max_time = self.counter[root.val]
            in_order(root.right)

        in_order(root)
        sorted_by_time = sorted(self.counter.items(), lambda item: item[1])
        return [_[0] for _ in self.counter.items() if _[1] == self.max_time]
# @lc code=end



#
# @lcpr case=start
# [1,null,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
