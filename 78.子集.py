#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode.cn/problems/subsets/description/
#
# algorithms
# Medium (81.20%)
# Likes:    2259
# Dislikes: 0
# Total Accepted:    743.5K
# Total Submissions: 915.3K
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
#
#
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        used = [False] * nums_len
        res = []
        def dfs(nums, size, depth, path, used, res):
            """
            深度优先搜索函数，用于生成所有可能的组合。

            :param nums: 给定的数字列表。
            :param size: 数字列表的大小。
            :param depth: 当前搜索的深度。
            :param path: 当前搜索路径。
            :param used: 标记哪些数字已被使用。
            :param res: 存储所有可能的组合结果。
            """
            # 当搜索深度等于列表大小时，将当前路径加入结果集
            res.append(path[:])
            return

            # 遍历数字列表，尝试将未使用的数字加入当前路径
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

            # # 遍历数字列表，尝试将未使用的数字加入当前路径
            # for i in range(size):
            #     if not used[i]:
            #         used[i] = True
            #         path.append(nums[i])

            #         # 递归进行下一层搜索
            #         dfs(nums, size, depth + 1, path, used, res)

            #         # 回溯：撤销上一步操作，标记该数字为未使用
            #         used[i] = False
            #         path.pop()
        dfs(nums, nums_len, 0, [], used, res)
        return res
# @lc code=end
