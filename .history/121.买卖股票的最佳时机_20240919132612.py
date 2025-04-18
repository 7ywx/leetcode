#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (57.69%)
# Likes:    3452
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 2.4M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
#
#
#
# 示例 1：
#
#
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#
#
# 示例 2：
#
#
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
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
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # v2.1 前缀最小值 78ms 97%
        minprice = int(1e5)  # 初始化最小价格为一个较大的数
        maxprofit = 0  # 初始化最大利润为0

        for price in prices:
            # 每天计算当前价格（当前卖出的价格）与之前最小价格的差值，与当前最大利润比较，取较大值。
            if price - minprice > maxprofit:
                maxprofit = price - minprice
            # 如果当前价格小于最小价格，则更新最小价格。
            if price < minprice:
                minprice = price

        return maxprofit

        # v1.2 动态规划 400ms 10%
        n = len(prices)
        # dp[i][0] 表示第i天持有股票时的最大利润。
        # dp[i][1] 表示第i天不持有股票时的最大利润。
        dp = [[0] * 2 for _ in range(n)]

        for i in range(n):
            # 初始化第一天的持有和不持有股票的最大利润。
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue

            # 计算每一天的最大利润。
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])

        # 返回最后一天不持有股票时的最大利润。
        return dp[n - 1][0]

        # v2.0 后缀最大价格 190ms 30%
        # 初始化利润为0，并创建一个字典用于存储每个位置后的最大价格
        profit = 0
        suffixMax = {}

        # 确保最后一个位置后的最大价格为0
        suffixMax[len(prices) - 1] = 0

        # 从倒数第二天开始向前遍历，计算每个位置后的最大价格
        for i in range(len(prices)-2, -1, -1):
            if prices[i+1] > suffixMax[i+1]:
                suffixMax[i] = prices[i+1]
            else:
                suffixMax[i] = suffixMax[i+1]

        # 重新初始化利润为0，然后遍历列表计算最大利润
        profit = 0
        for i in range(len(prices)-1):
            # 今天买入后，计算今天卖出的最大利润
            if suffixMax[i] - prices[i] > profit:
                profit = suffixMax[i] - prices[i]
        return profit

        # v1.1 暴力解法 200/212 未通过
        profit = 0
        for i in range(len(prices)-1):
            if max(prices[i+1:]) - prices[i] > profit:
                profit = max(prices[i+1:]) - prices[i]
        return profit

        # v1.0 暴力解法 199/212 未通过
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if (prices[j] - prices[i]) > profit:
                    profit = prices[j] - prices[i]
        return profit
# @lc code=end
s = Solution()
s.maxProfit([7,1,5,3,6,4])
