#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# https://leetcode.cn/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (55.59%)
# Likes:    3611
# Dislikes: 0
# Total Accepted:    904.8K
# Total Submissions: 1.6M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7]
# 的子序列。
#
#
# 示例 1：
#
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#
#
# 示例 2：
#
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#
#
# 示例 3：
#
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
#
#
# 进阶：
#
#
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
#
#
#
from typing import List
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # k神 二分
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res

        # 自己写的
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            maxLen = 1
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i] and dp[j] + 1 > maxLen:
                    maxLen = dp[j] + 1
            dp[i] = maxLen
        return max(dp)


        n = len(nums)
        dp = [1] * n  # 创建一个长度为n的数组，用于存储以每个元素为结尾的最长递增子序列的长度，初始值都为1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:  # 如果当前元素nums[i]大于nums[j]
                    dp[i] = max(dp[i], dp[j] + 1)  # 更新以nums[i]为结尾的最长递增子序列的长度
        return max(dp)  # 返回dp数组中的最大值，即最长递增子序列的长度
# @lc code=end
s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
# print(s.lengthOfLIS([0,1,0,3,2,3]))
