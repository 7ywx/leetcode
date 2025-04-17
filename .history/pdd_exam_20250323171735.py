from functools import lru_cache

def count_lucky_up_to(X: int) -> int:
    """计算 1 到 X 内的幸运数数量"""
    if X <= 0:
        return 0

    digits = list(map(int, str(X)))  # 将X拆成数位列表
    n = len(digits)

    @lru_cache(None)
    def dp(pos: int, mod: int, limit: bool) -> int:
        """数位DP递归：
        pos - 当前处理到哪一位
        mod - 当前前缀数位和 mod 3
        limit - 是否受限（是否必须小于等于X）
        """
        if pos == n:
            return 1 if mod == 0 else 0  # 终止条件：如果某个前缀子串是3的倍数，算一个幸运数

        up = digits[pos] if limit else 9  # 当前位的上限（受X限制）
        res = 0

        for d in range(up + 1):  # 枚举当前位填 d
            res += dp(pos + 1, (mod + d) % 3, limit and d == up)

        return res

    return dp(0, 0, True)

def lucky_numbers_in_range(L: int, R: int) -> int:
    """计算区间 [L, R] 内的幸运数数量"""
    return count_lucky_up_to(R) - count_lucky_up_to(L - 1)

# 测试
L, R = 2, 45
print(lucky_numbers_in_range(L, R))  # 输出区间 [10, 100] 内的幸运数数量
