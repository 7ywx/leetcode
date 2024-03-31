#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode.cn/problems/coin-change/description/
#
# algorithms
# Medium (47.94%)
# Likes:    2791
# Dislikes: 0
# Total Accepted:    793.6K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,5]\n11'
#
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
#
#
# 示例 1：
#
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
# 示例 2：
#
#
# 输入：coins = [2], amount = 3
# 输出：-1
#
# 示例 3：
#
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#
from typing import List
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount+1] * amount # dp[i]表示凑成i所需要的最小硬币数, amount+1表示不可达状态
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    # dp[i] = min(dp[i], dp[i-coin]+1)
                    if dp[i-coin] + 1 < dp[i]:
                        dp[i] = dp[i-coin] + 1
        return dp[-1] if dp[-1] != amount+1 else -1

        # # 每次都找最大的匹配的硬币, 贪心算法？
        # coins.sort()
        # coinsNum = 0
        # found = False
        # while amount > 0:
        #     found = False
        #     for i in range(len(coins)-1, -1, -1):
        #         if amount >= coins[i]:
        #             amount -= coins[i]
        #             coinsNum += 1
        #             found = True
        #             break
        #     if not found:
        #         return -1
        # return coinsNum
# @lc code=end
s = Solution()
# print(s.coinChange([1,2,5], 11))
# print(s.coinChange([2], 3))
print(s.coinChange([186,419,83,408], 6249))
