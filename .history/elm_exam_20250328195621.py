# from collections import Counter

# def can_rearrange_to_eleme(s: str) -> bool:
#     # 统计字符数量
#     count = Counter(s)
#     e_count = count.get('e', 0)
#     l_count = count.get('l', 0)
#     m_count = count.get('m', 0)

#     # 检查基本约束
#     # 条件1：'e' 的数量不能超过总长度的一半（向上取整）
#     if e_count > (len(s) + 1) // 2:
#         return False

#     # 条件2：'l' 和 'm' 的数量之和不能超过 'e' 的数量加 1
#     if l_count + m_count > e_count + 1:
#         return False

#     # 条件3：'l' 和 'm' 的数量不能相差太多
#     if abs(l_count - m_count) > 1:
#         return False

#     # 如果以上条件都满足，则可以重新排列为合法字符串
#     return True

# # 测试用例
# print(can_rearrange_to_eleme("eeelm"))  # True
# print(can_rearrange_to_eleme("eeelme"))  # False


def can_form_eleme_string(s):
    from collections import Counter

    # 统计字符频率
    count = Counter(s)
    e_count = count['e']
    l_count = count['l']
    m_count = count['m']

    # 检查 e 是否过多
    if e_count > (len(s) + 1) // 2:
        return False, ""

    # 构造字符串
    result = []
    other_chars = list('l' * l_count + 'm' * m_count)  # 将 l 和 m 合并
    e_remaining = e_count

    # 先尽可能插入 e，再插入其他字符
    while e_remaining > 0 or other_chars:
        # 插入 e
        if e_remaining > 0:
            result.append('e')
            e_remaining -= 1

        # 插入其他字符
        if other_chars:
            result.append(other_chars.pop())

    # 转为字符串并检查是否有非法子串
    final_str = ''.join(result)
    if any(sub in final_str for sub in ['ee', 'lm', 'ml', 'll', 'mm']):
        return False, ""

    return True, final_str

# 测试
s = "eeelm"
can_form, rearranged = can_form_eleme_string(s)
print("Can form eleme string:", can_form)
if can_form:
    print("Rearranged string:", rearranged)
