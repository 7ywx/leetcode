#
# @lc app=leetcode.cn id=654 lang=python3
# @lcpr version=30104
#
# [654] 最大二叉树
#
# https://leetcode.cn/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (82.46%)
# Likes:    836
# Dislikes: 0
# Total Accepted:    293.9K
# Total Submissions: 356.4K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
#
#
# 创建一个根节点，其值为 nums 中的最大值。
# 递归地在最大值 左边 的 子数组前缀上 构建左子树。
# 递归地在最大值 右边 的 子数组后缀上 构建右子树。
#
#
# 返回 nums 构建的 最大二叉树 。
#
#
#
# 示例 1：
#
# 输入：nums = [3,2,1,6,0,5]
# 输出：[6,3,5,null,2,0,null,null,1]
# 解释：递归调用如下所示：
# - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
# ⁠   - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
# ⁠       - 空数组，无子节点。
# ⁠       - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
# ⁠           - 空数组，无子节点。
# ⁠           - 只有一个元素，所以子节点是一个值为 1 的节点。
# ⁠   - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
# ⁠       - 只有一个元素，所以子节点是一个值为 0 的节点。
# ⁠       - 空数组，无子节点。
#
#
# 示例 2：
#
# 输入：nums = [3,2,1]
# 输出：[3,null,2,null,1]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# nums 中的所有整数 互不相同
#
#
#
from typing import Optional, List
from 层序遍历构造二叉树 import levelOrder, preorder
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # if not nums:
        #     return TreeNode()
        max_idx = nums.index(max(nums))
        root = TreeNode(nums[max_idx])
        root.left = self.constructMaximumBinaryTree(nums[:max_idx]) if max_idx > 0 else None
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:]) if max_idx < len(nums)-1 else None
        return root
# @lc code=end



#
# @lcpr case=start
# [3,2,1,6,0,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end
s = Solution()
root = s.constructMaximumBinaryTree([3,2,1])
levelOrder(root)
print(preorder(root))
#
