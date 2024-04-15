#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
# https://leetcode.cn/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (21.19%)
# Likes:    1783
# Dislikes: 0
# Total Accepted:    620.2K
# Total Submissions: 2.9M
# Testcase Example:  '"42"'
#
# 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
#
# 函数 myAtoi(string s) 的算法如下：
#
#
# 读入字符串并丢弃无用的前导空格
# 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
# 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
# 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤
# 2 开始）。
# 如果整数数超过 32 位有符号整数范围 [−2^31,  2^31 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −2^31
# 的整数应该被固定为 −2^31 ，大于 2^31 − 1 的整数应该被固定为 2^31 − 1 。
# 返回整数作为最终结果。
#
#
# 注意：
#
#
# 本题中的空白字符只包括空格字符 ' ' 。
# 除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "42"
# 输出：42
# 解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
# 第 1 步："42"（当前没有读入字符，因为没有前导空格）
# ⁠        ^
# 第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
# ⁠        ^
# 第 3 步："42"（读入 "42"）
# ⁠          ^
# 解析得到整数 42 。
# 由于 "42" 在范围 [-2^31, 2^31 - 1] 内，最终结果为 42 。
#
# 示例 2：
#
#
# 输入：s = "   -42"
# 输出：-42
# 解释：
# 第 1 步："   -42"（读入前导空格，但忽视掉）
# ⁠           ^
# 第 2 步："   -42"（读入 '-' 字符，所以结果应该是负数）
# ⁠            ^
# 第 3 步："   -42"（读入 "42"）
# ⁠              ^
# 解析得到整数 -42 。
# 由于 "-42" 在范围 [-2^31, 2^31 - 1] 内，最终结果为 -42 。
#
#
# 示例 3：
#
#
# 输入：s = "4193 with words"
# 输出：4193
# 解释：
# 第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格）
# ⁠        ^
# 第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
# ⁠        ^
# 第 3 步："4193 with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止）
# ⁠            ^
# 解析得到整数 4193 。
# 由于 "4193" 在范围 [-2^31, 2^31 - 1] 内，最终结果为 4193 。
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 200
# s 由英文字母（大写和小写）、数字（0-9）、' '、'+'、'-' 和 '.' 组成
#
#
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # 去除开头的空格
        s = s.lstrip()

        if not s:
            return 0  # 字符串为空，返回0

        # 处理符号
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # 读取数字，直到遇到非数字字符
        num = 0
        for char in s:
            if char.isdigit(): #TODO python备忘录-函数
                num = num * 10 + int(char)
            else:
                break

        # 根据符号和范围返回结果
        num *= sign
        return max(min(num, 2**31 - 1), -2**31)

        """
        解析字符串中的数字，并根据数字的范围返回相应的结果。

        参数:
        s: 待解析的字符串。

        返回值:
        返回解析出的数字。如果数字超出INT_MAX（32位整数的最大值）则返回INT_MAX，
        如果数字低于INT_MIN（32位整数的最小值）则返回INT_MIN，如果字符串中没有数字则返回0。
        """
        num = [str(i) for i in range(10)]  # 生成数字字符串列表
        result = ''  # 初始化结果字符串
        INT_MAX = 2**31 - 1  # 定义INT_MAX
        INT_MIN = -2**31  # 定义INT_MIN
        flag = 0  # 初始化标志变量，用于标识是否开始解析数字

        # 遍历字符串
        for index in range(len(s)):
            if s[index] == ' ' and flag == 0:  # 忽略字符串中的空格
                continue
            elif s[index] in ['-','+'] and flag!=1 and index+1<len(s) and s[index+1] in num:  # 遇到符号且后面跟着数字
                flag = 1
                result += s[index]
            elif s[index] in num:  # 遇到数字
                flag = 1
                result += s[index]
            else:  # 遇到非数字字符，解析结束
                if result != '':  # 如果结果非空
                    if int(result) > INT_MAX:  # 检查是否超出INT_MAX
                        return INT_MAX
                    if int(result) < INT_MIN:  # 检查是否低于INT_MIN
                        return INT_MIN
                    return int(result)  # 返回解析结果
                else:  # 如果结果为空
                    return 0  # 返回0

        if result != '':  # 如果循环结束后结果非空
            if int(result) > INT_MAX:  # 再次检查是否超出INT_MAX
                return INT_MAX
            if int(result) < INT_MIN:  # 再次检查是否低于INT_MIN
                return INT_MIN
            return int(result)  # 返回最终解析结果
        else:  # 如果结果为空
            return 0  # 返回0
# @lc code=end
solution = Solution()
print(solution.myAtoi("00000-42a1234"))
