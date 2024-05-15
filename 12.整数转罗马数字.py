#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#
# https://leetcode.cn/problems/integer-to-roman/description/
#
# algorithms
# Medium (67.08%)
# Likes:    1286
# Dislikes: 0
# Total Accepted:    476.1K
# Total Submissions: 709.7K
# Testcase Example:  '3749'
#
# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
#
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
#
#
# 给你一个整数，将其转为罗马数字。
#
#
#
# 示例 1:
#
#
# 输入: num = 3
# 输出: "III"
#
# 示例 2:
#
#
# 输入: num = 4
# 输出: "IV"
#
# 示例 3:
#
#
# 输入: num = 9
# 输出: "IX"
#
# 示例 4:
#
#
# 输入: num = 58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.
#
#
# 示例 5:
#
#
# 输入: num = 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
#
#
# 提示：
#
#
# 1
#
#
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        """
        将整数转换为罗马数字表示。

        参数:
        num -- 要转换的整数，必须大于等于 0。

        返回值:
        res -- 表示整数 num 的罗马数字字符串。
        """
        res = ''  # 初始化结果字符串
        romans = ['IV', 'XL', 'CD', 'M']  # 罗马数字对应的四个基本单元
        w = 0  # 计数器，用于选择基本单元
        while num != 0:  # 当 num 不为零时，持续转换
            num, m = divmod(num, 10)  # 分别得到当前数的十位和个位
            if w < 3:  # 对于前三个基本单元（I, X, C），有额外的规则处理
                if 1 <= m <= 3:  # 当个位数为 1 到 3 时，重复使用基本单元的第一个字符
                    res = romans[w][0] * m + res
                elif m == 4:  # 当个位数为 4 时，使用当前基本单元加下一个基本单元的第一个字符
                    res = romans[w] + res
                elif m == 5:  # 当个位数为 5 时，使用当前基本单元的第二个字符
                    res = romans[w][1] + res
                elif 6 <= m <= 8:  # 当个位数为 6 到 8 时，使用当前基本单元的第二个字符加上一定数量的第一个字符
                    res = romans[w][1] + romans[w][0] * (m-5) + res
                elif m == 9:  # 当个位数为 9 时，使用当前基本单元的第一个字符加上下一个基本单元的第一个字符
                    res = romans[w][0] + romans[w+1][0] + res
            else:  # 对于第四个基本单元（M），直接重复使用来表示更大的数值
                res = 'M' * m + res
            w += 1  # 更新基本单元索引
        return res

        # roman = ''
        # intToRomanMap = {
        #     1000: 'M',
        #     900: 'CM',
        #     500: 'D',
        #     400: 'CD',
        #     100: 'C',
        #     90: 'XC',
        #     50: 'L',
        #     40: 'XL',
        #     10: 'X',
        #     9: 'IX',
        #     8: 'VIII',
        #     5: 'V',
        #     4: 'IV',
        #     1: 'I'
        # }
        # for value, symbol in sorted(intToRomanMap.items(), reverse=True):
        #     while num >= value:
        #         roman += symbol
        #         num -= value
        # return roman

        # roman = ''
        # while num:
        #     if num >=1000: # [1000, 3999]
        #         roman += 'M'
        #         num -= 1000
        #     elif num >= 900: # [900, 999]
        #         roman += 'CM'
        #         num -= 900
        #     elif num >= 500: # [500, 899]
        #         roman += 'D'
        #         num -= 500
        #     elif num >= 400: # [400, 499]
        #         roman += 'CD'
        #         num -= 400
        #     elif num >= 100: # [100, 399]
        #         roman += 'C'
        #         num -= 100
        #     elif num >= 90: # [90, 99]
        #         roman += 'XC'
        #         num -= 90
        #     elif num >= 50: # [50, 89]
        #         roman += 'L'
        #         num -= 50
        #     elif num >= 40: # [40, 49]
        #         roman += 'XL'
        #         num -= 40
        #     elif num >= 10: # [10, 39]
        #         roman += 'X'
        #         num -= 10
        #     elif num >= 9: # [9, 9]
        #         roman += 'IX'
        #         num -= 9
        #     elif num >= 5: # [5, 8]
        #         roman += 'V'
        #         num -= 5
        #     elif num >= 4: # [4, 4]
        #         roman += 'IV'
        #         num -= 4
        #     elif num >= 1: # [1, 3]
        #         roman += 'I'
        #         num -= 1
        # return roman
# @lc code=end
