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
from typing import List, Optional
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #TODO 过于烧脑
        def backtrack(start, path):
            # 将当前路径添加到结果集中
            result.append(path[:])

            # 递归处理下一个元素
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # 回溯，移除当前元素

        result = []
        backtrack(0, [])
        return result
# @lc code=end
solution = Solution()
print(solution.subsets([1,2,3]))
