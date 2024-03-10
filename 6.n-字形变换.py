#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#
# https://leetcode.cn/problems/zigzag-conversion/description/
#
# algorithms
# Medium (52.39%)
# Likes:    2254
# Dislikes: 0
# Total Accepted:    632.6K
# Total Submissions: 1.2M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
#
# string convert(string s, int numRows);
#
#
#
# 示例 1：
#
#
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
#
# 示例 2：
#
#
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# 示例 3：
#
#
# 输入：s = "A", numRows = 1
# 输出："A"
#
#
#
#
# 提示：
#
#
# 1
# s 由英文字母（小写和大写）、',' 和 '.' 组成
# 1
#
#
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #chatgpt
        # # 如果只有一行或行数大于等于字符串长度，直接返回原字符串
        # if numRows == 1 or numRows >= len(s):
        #     return s

        # # 创建一个列表，用于存储每一行的字符串
        # result = [''] * numRows
        # print(result)
        # index, step = 0, 1  # index表示当前行的索引，step表示行索引的变化方向

        # # 遍历原始字符串
        # for char in s:
        #     # 将字符添加到相应行的字符串中
        #     result[index] += char
        #     # 根据Z字形变换的规律更新行索引和方向
        #     if index == 0:
        #         step = 1  # 当索引到达最顶部时，行索引向下移动
        #     elif index == numRows - 1:
        #         step = -1  # 当索引到达最底部时，行索引向上移动
        #     index += step

        # # 将每一行的字符串连接起来得到最终结果
        # print(result)
        # return ''.join(result)

        # 最优解
        # 如果numRows小于2，则直接返回该字符串
        if numRows < 2:
            return s
        # 创建一个空列表，列数与numRows相同。第i列存储转换后第i行的字符
        res = ["" for _ in range(numRows)]
        # 当前元素转换后在第i行
        i = 0
        # flag表示当前处于 Z 字形排列的方向（+1：向下移动，-1：向上移动）
        flag = -1
        # 遍历给定字符串的每个字符
        for c in s:
            # 将字符c添加到res列表的第i列
            res[i] += c
            # 如果i等于0或numRows-1（即将要遍历最后一行），则将标志位flag取反
            if i == 0 or i == numRows-1:
                flag = -flag
            # 将索引值i更新为下一个位置
            i += flag
        # 将res列表中的字符串连接成一个字符串，并返回
        return "".join(res)

    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows == 1:
    #         return s
    #     else:
    #         rowNum = ((len(s) // (2 * numRows - 2)) + 1) * numRows
    #         s2d = [[''] * rowNum for _ in range(numRows)]
    #         for i in range(len(s)):
    #             row = i // (2 * numRows - 2)
    #             if i < row * (2 * numRows - 2) + numRows:
    #                 s2d[i-(row * (2*numRows - 2))][row * (numRows - 1)] = s[i]
    #             else:
    #                 s2d[numRows-1-(i-(numRows -1 + row*(2*numRows-2)))][i-(numRows -1 + row*(2*numRows-2))+row * (numRows - 1)] = s[i]
    #         result = []
    #         for row in s2d:
    #             for element in row:
    #                 if element != '':
    #                     result.append(element)
    #         # print(''.join(result))
    #         return ''.join(result)
# @lc code=end
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))
print("--")
# print(solution.convert("PAYPALISHIRING", 4))
# print(solution.convert("A", 1))
