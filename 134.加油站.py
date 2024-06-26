#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
# https://leetcode.cn/problems/gas-station/description/
#
# algorithms
# Medium (47.82%)
# Likes:    1606
# Dislikes: 0
# Total Accepted:    362.1K
# Total Submissions: 758K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一
# 的。
#
#
#
# 示例 1:
#
#
# 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
#
# 示例 2:
#
#
# 输入: gas = [2,3,4], cost = [3,4,3]
# 输出: -1
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。
#
#
#
# 提示:
#
#
# gas.length == n
# cost.length == n
# 1 <= n <= 10^5
# 0 <= gas[i], cost[i] <= 10^4
#
#
#
from typing import List
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        寻找最小的开始位置，使得从该位置开始能够遍历整个gas列表而不需要额外的燃料。

        参数:
        gas -- 一个整数列表，表示每个加油站提供的燃料量。
        cost -- 一个整数列表，表示从一个加油站到下一个加油站所需的燃料成本。

        返回值:
        如果能找到一个位置，使得从该位置开始能够遍历整个gas列表，返回最小的开始位置索引；
        如果不能完成遍历，返回-1。
        """
        # 计算每个加油站的剩余燃料，即提供的燃料量减去到该加油站的成本
        rest = [g - c for g, c in zip(gas, cost)]
        # 如果所有加油站的剩余燃料总和小于0，表示无法遍历整个列表，返回-1
        if sum(rest) < 0:
            return -1
        # 初始化油箱中的燃料量和开始位置
        tank = 0
        start = 0
        # 遍历每个加油站的剩余燃料，累计油箱中的燃料量
        for i, r in enumerate(rest):
            tank += r
            # 如果油箱中的燃料量小于0，说明从开始位置到当前位置的加油站无法遍历，更新开始位置
            if tank < 0:
                tank = 0
                start = i + 1
        return start

        # # 暴力法 v1 超时
        # n = len(gas)
        # def check(i):
        #     tank = 0
        #     for j in range(i, i + n):
        #         tank += gas[j % n] - cost[j % n]
        #         if tank < 0:
        #             return False
        #     return True
        # for i, g in enumerate(gas):
        #     if g < cost[i] or g == 0:
        #         continue
        #     if check(i):
        #         return i
        #     # flag = 1
        #     # while flag:
        #     #     tank = 0 # 油箱油量
        #     #     for j in range(i, i + n):
        #     #         tank += gas[j % n] - cost[j % n]
        #     #         if tank < 0:
        #     #             flag = 0
        #     #             break
        #     #     if flag:
        #     #         return i
        # return -1
# @lc code=end
s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
print(s.canCompleteCircuit([2,3,4], [3,4,3])) # -1
