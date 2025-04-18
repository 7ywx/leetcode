#
# @lc app=leetcode.cn id=450 lang=python3
# @lcpr version=30104
#
# [450] 删除二叉搜索树中的节点
#
# https://leetcode.cn/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (52.72%)
# Likes:    1424
# Dislikes: 0
# Total Accepted:    311.4K
# Total Submissions: 590K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key
# 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
#
# 一般来说，删除节点可分为两个步骤：
#
#
# 首先找到需要删除的节点；
# 如果找到了，删除它。
#
#
#
#
# 示例 1:
#
#
#
# 输入：root = [5,3,6,2,4,null,7], key = 3
# 输出：[5,4,6,2,null,null,7]
# 解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
# 另一个正确答案是 [5,2,6,null,4,null,7]。
#
#
#
#
# 示例 2:
#
# 输入: root = [5,3,6,2,4,null,7], key = 0
# 输出: [5,3,6,2,4,null,7]
# 解释: 二叉树不包含值为 0 的节点
#
#
# 示例 3:
#
# 输入: root = [], key = 0
# 输出: []
#
#
#
# 提示:
#
#
# 节点数的范围 [0, 10^4].
# -10^5 <= Node.val <= 10^5
# 节点值唯一
# root 是合法的二叉搜索树
# -10^5 <= key <= 10^5
#
#
#
#
# 进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。
#
#

from typing import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif root.left and root.right:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
            else:
                return root.left if root.left else root.right
        if root.val > key: root.left = self.deleteNode(root.left, key) # 每次递归调用都会返回调整后的子树根节点，最终返回整个树的根节点。
        else: root.right = self.deleteNode(root.right, key)
        return root
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [5,3,6,2,4,null,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,7]\n0\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
