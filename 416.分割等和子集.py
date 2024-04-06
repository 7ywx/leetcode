#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode.cn/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (52.39%)
# Likes:    2047
# Dislikes: 0
# Total Accepted:    528.3K
# Total Submissions: 1M
# Testcase Example:  '[1,5,11,5]'
#
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
#
# 示例 2：
#
#
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#
from typing import List
from collections import OrderedDict
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # v3 线性DP + 位运算优化
        s = sum(nums)
        if s & 1:
            return False
        target = s >> 1
        # dp的二进制数中，从左往右数，从0开始，第i位表示能否组成和为i的集合
        dp = 1 << target
        print(dp)
        for x in nums:
            dp |= dp >> x
            # 提前返回答案
            if dp & 1:
                return True
        return False

        # v2 一维（线性）DP
        # if n < 2:
        #     return False
        # target, is1 = divmod(sum(nums), 2)
        # if is1:
        #     return False
        if sum(nums) & 1: # 如果数组元素和为奇数，则无法分割成两个相等的子集。
            return False
        target = sum(nums) >> 1

        # if target in nums:
        #     return True

        # dp[j]表示数组能否组成总和为j的子集。
        dp = [True] + [False] * target # 初始化dp[0]为True，因为不选取任何元素时，总和为0是可能的。

        # for i in range(target + 1):
        #     print(i, end="      ")
        # print()
        # print(dp)

        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]
            # print(dp)
        return dp[-1]

        # v1 二维DP
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][target]

        # hashtable = OrderedDict({0: True, nums[0]: True})
        # prefixSum = [nums[0]]


        # for i in range(1, len(nums)):
        #     prefixSum.append(prefixSum[-1] + nums[i])
        #     hashtable[prefixSum[-1]] = True

        # print(prefixSum, hashtable)

        # if prefixSum[-1] % 2 != 0:
        #     return False

        # target = prefixSum[-1] // 2
        # for i in range(len(prefixSum)):
        #     if prefixSum[i] - target in hashtable:
        #         return True
        # return False

        # suffixSum = nums[:]
        # for i in range(len(nums)-2, -1, -1):
        #     suffixSum[i] = (suffixSum[i+1] + nums[i])
        # print(prefixSum, suffixSum)
# @lc code=end
s = Solution()
print(s.canPartition([1,5,11,5]))
print(s.canPartition([1,7,3,5]))

"""
按位与运算（Bitwise AND operation）是一种基本的二进制算术运算，它应用于两个相同长度的二进制数（通常是整数），逐位比较并产生一个新的二进制数作为结果。按位与运算的主要意义和应用包括以下几个方面：

筛选特定位：

通过与一个称为掩码（mask）的特定二进制模式进行按位与运算，可以提取或保留原数值中符合掩码设定的位，同时清除其他位。掩码通常是一串二进制数，其中希望保留的位设置为1，其余位设置为0。这在很多计算机系统和网络协议中用于提取或设置特定位字段（bit field），比如IP地址中的网络部分、端口号中的保留位等。
检测位状态：

利用按位与运算检查某个数值的特定位是否为1。例如，若要确定一个整数的最低位（最右边的位）是否为1，可以将其与数值1（二进制表示为0000...0001）进行按位与运算。如果结果非零，则说明最低位为1，否则为0。
权限控制（位标志/标志位）：

在软件开发中，尤其是操作系统和数据库系统，常使用按位与运算来管理权限或状态标志。一个整数的各个位可以代表不同的权限或状态，通过对这个整数进行按位与操作，可以快速判断用户或进程是否具有特定权限，或者某项状态是否已设置。
数据压缩与编码：

在某些数据编码方案中，按位与运算可用于有效地压缩信息。当多个数据项的某些位存在固定模式时，可以将这些位合并到一个整数中，通过按位与运算提取所需信息。
高效算法实现：

在算法设计中，按位与运算有时能提供简洁高效的解决方案。例如，求解一个数是否为2的幂可以通过将其与自身减1进行按位与运算，若结果为0，则该数为2的幂。此外，某些位计数、位翻转等问题也能借助按位与运算简化计算。
硬件级别操作：

在底层硬件控制和微处理器指令集中，按位与运算是非常基础的操作之一，常用于寄存器操作、内存地址映射、中断屏蔽等场合，能够直接作用于机器级别的二进制数据。
综上所述，按位与运算因其在二进制层面精确控制单个位的能力，在计算机科学的诸多领域发挥着重要作用，包括数据处理、通信协议、权限管理、算法优化及硬件控制等方面。通过按位与运算，可以高效、精准地操作二进制数据的各个位，实现诸如筛选、检测、编码、控制等多种功能。
"""
