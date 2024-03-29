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
        # 前缀最小值
        minprice = int(1e5)
        maxprofit = 0
        for price in prices:
            # maxprofit = max(price - minprice, maxprofit)
            # minprice = min(minprice, price)
            if price - minprice > maxprofit:
                maxprofit = price - minprice
            if price < minprice:
                minprice = price
            print(f'maxprofit = {maxprofit}, minprice = {minprice}')
        return maxprofit

        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n)]
        # for i in range(n):
        #     if i - 1 == -1:
        #         # base case
        #         dp[i][0] = 0
        #         dp[i][1] = -prices[i]
        #         continue
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #     dp[i][1] = max(dp[i - 1][1], -prices[i])
        # return dp[n - 1][0]

        # # 初始化利润为0，并创建一个字典用于存储每个位置后的最大价格
        # profit = 0
        # suffixMax = {}
        # # 确保最后一个位置后的最大价格为0
        # suffixMax[len(prices) - 1] = 0
        # # 从倒数第二天开始向前遍历，计算每个位置后的最大价格
        # for i in range(len(prices)-2, -1, -1):
        #     if prices[i+1] > suffixMax[i+1]:
        #         suffixMax[i] = prices[i+1]
        #     else:
        #         suffixMax[i] = suffixMax[i+1]
        # # 重新初始化利润为0，然后遍历列表计算最大利润
        # profit = 0
        # for i in range(len(prices)-1):
        #     if suffixMax[i] - prices[i] > profit:
        #         profit = suffixMax[i] - prices[i]
        # return profit

        # profit = 0
        # for i in range(len(prices)-1):
        #     if max(prices[i+1:]) - prices[i] > profit:
        #         profit = max(prices[i+1:]) - prices[i]
        # return profit

        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if (prices[j] - prices[i]) > profit:
        #             profit = prices[j] - prices[i]
        # return profit
# @lc code=end
s = Solution()
s.maxProfit([7,1,5,3,6,4])
