#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
# https://leetcode.cn/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (54.39%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    74.8K
# Total Submissions: 137.5K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# 基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。
#
# 假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。
#
#
# 例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
#
#
# 另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中）
#
# 给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end
# 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。
#
# 注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。
#
#
#
# 示例 1：
#
#
# 输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# 输出：1
#
#
# 示例 2：
#
#
# 输入：start = "AACCGGTT", end = "AAACGGTA", bank =
# ["AACCGGTA","AACCGCTA","AAACGGTA"]
# 输出：2
#
#
# 示例 3：
#
#
# 输入：start = "AAAAACCC", end = "AACCCCCC", bank =
# ["AAAACCCC","AAACCCCC","AACCCCCC"]
# 输出：3
#
#
#
#
# 提示：
#
#
# start.length == 8
# end.length == 8
# 0 <= bank.length <= 10
# bank[i].length == 8
# start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成
#
#
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        计算从开始基因到结束基因的最小变异步数。

        :param startGene: 开始基因序列
        :param endGene: 结束基因序列
        :param bank: 一个字符串列表，包含所有可能的基因序列
        :return: 返回最小变异步数，如果不可能到达则返回-1
        """
        # 如果开始基因和结束基因相同，则不需要变异，直接返回0
        if start == end:
            return 0

        # 将银行基因列表转换为集合，以便快速查找
        bank = set(bank)

        # 如果结束基因不在银行基因集合中，则无法通过变异到达，直接返回-1
        if end not in bank:
            return -1

        # 使用双端队列来进行广度优先搜索，存储当前基因和变异步数
        q = deque([(start, 0)])

        # 当队列不为空时，继续搜索
        while q:
            # 从队列中取出当前基因和当前变异步数
            cur, step = q.popleft()

            # 遍历当前基因的每个位置
            for i, x in enumerate(cur):
                # 遍历ACGT四种基因
                for y in "ACGT":
                    # 如果当前位置的基因不等于y，则进行变异
                    if y != x:
                        # 变异后的基因序列
                        nxt = cur[:i] + y + cur[i + 1:]

                        # 如果变异后的基因在银行基因集合中
                        if nxt in bank:
                            print(f"nxt:{nxt}, step:{step}, i:{i}, x:{x}")
                            # 如果变异后的基因等于结束基因，则返回当前变异步数+1
                            if nxt == end:
                                return step + 1

                            # 从银行基因集合中移除已经变异过的基因
                            bank.remove(nxt)

                            # 将变异后的基因和变异步数+1存入队列
                            q.append((nxt, step + 1))
                            print(f"q:{q}")


        # 如果搜索完所有可能的基因变异，仍然没有到达结束基因，返回-1
        return -1
# @lc code=end
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Solution().minMutation(start, end, bank)
