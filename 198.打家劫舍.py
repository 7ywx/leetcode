#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode.cn/problems/house-robber/description/
#
# algorithms
# Medium (54.95%)
# Likes:    2960
# Dislikes: 0
# Total Accepted:    948.8K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,1]'
#
#
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#
#
#
# 示例 1：
#
#
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
# 示例 2：
#
#
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#
#
#
#
# 提示：
#
#
# 1
# 0
#
#
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态规划v2 貌似先分配空间还能快一点
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            # nums[0]: 抢0不抢1 numms[1]: 抢1不抢0
            dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # dpp[i-2]+nums[i]: 抢i不抢i-1 dp[i-1]: 抢i-1不抢i
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

        # 动态规划v1
        dp = [nums[0]]
        if len(nums) > 1:
            # nums[0]: 抢0不抢1 numms[1]: 抢1不抢0
            dp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            # dpp[i-2]+nums[i]: 抢i不抢i-1 dp[i-1]: 抢i-1不抢i
            dp.append(max(dp[i-2]+nums[i], dp[i-1]))
        return dp[-1]
# @lc code=end
