from collections import Counter

def can_rearrange_to_eleme(s: str) -> bool:
    # 统计字符数量
    count = Counter(s)
    e_count = count.get('e', 0)
    l_count = count.get('l', 0)
    m_count = count.get('m', 0)

    # 检查基本约束
    # 条件1：'e' 的数量不能超过总长度的一半（向上取整）
    if e_count > (len(s) + 1) // 2:
        return False

    # 条件2：'l' 和 'm' 的数量之和不能超过 'e' 的数量加 1
    if l_count + m_count > e_count + 1:
        return False

    # 条件3：'l' 和 'm' 的数量不能相差太多
    if abs(l_count - m_count) > 1:
        return False

    # 如果以上条件都满足，则可以重新排列为合法字符串
    return True

# 测试用例
print(can_rearrange_to_eleme("eeelm"))  # True
print(can_rearrange_to_eleme("eeelme"))  # False
