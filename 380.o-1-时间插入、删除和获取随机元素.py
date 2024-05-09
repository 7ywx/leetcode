#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#
# https://leetcode.cn/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (52.20%)
# Likes:    822
# Dislikes: 0
# Total Accepted:    162.2K
# Total Submissions: 310.7K
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n' +
  '[[],[1],[2],[2],[],[1],[2],[]]'
#
# 实现RandomizedSet 类：
#
#
#
#
# RandomizedSet() 初始化 RandomizedSet 对象
# bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
# bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
# int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
#
#
# 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。
#
#
#
# 示例：
#
#
# 输入
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove",
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# 输出
# [null, true, false, true, 2, true, false, 2]
#
# 解释
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
# randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
# randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
# randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
#
#
#
#
# 提示：
#
#
# -2^31 <= val <= 2^31 - 1
# 最多调用 insert、remove 和 getRandom 函数 2 * 10^5 次
# 在调用 getRandom 方法时，数据结构中 至少存在一个 元素。
#
#
#
#
#
import random
# @lc code=start
class RandomizedSet:
    """
    实现一个随机集合，支持插入、删除和获取一个随机元素的操作。
    """

    def __init__(self):
        """
        初始化随机集合。
        """
        # 使用字典存储元素及其存在状态，以支持快速查找
        self.random_set = {}
        # 使用列表存储元素，以支持随机访问
        self.random_set_list = []

    def insert(self, val: int) -> bool:
        """
        向随机集合中插入一个元素。

        参数:
        val (int): 需要插入的元素值。

        返回:
        bool: 如果插入成功返回True，如果元素已存在返回False。
        """
        # 检查元素是否已存在，若存在则不插入
        if val in self.random_set:
            return False
        # 插入元素到字典和列表中
        self.random_set[val] = 1
        self.random_set_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        从随机集合中删除一个元素。

        参数:
        val (int): 需要删除的元素值。

        返回:
        bool: 如果删除成功返回True，如果元素不存在返回False。
        """
        # 检查元素是否存在于集合中，若不存在则不删除
        if val not in self.random_set:
            return False
        # 从字典和列表中删除元素
        del self.random_set[val]
        self.random_set_list.remove(val)
        return True

    def getRandom(self) -> int:
        """
        随机返回集合中的一个元素。

        返回:
        int: 集合中的一个随机元素。
        """
        # 从列表中随机选择一个元素返回
        return random.choice(self.random_set_list) # TODO random.choice() 方法返回一个列表，元组或字符串的随机项。


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
