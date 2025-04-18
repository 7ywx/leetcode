def is_lucky(num: int) -> bool:
    s = str(num)
    n = len(s)
    # 如果数位数 >= 3，必然幸运
    if n >= 3:
        return True

    # 对于一位数，只有 0, 3, 6, 9 幸运
    if n == 1:
        return num in {0, 3, 6, 9}

    # 对于两位数，检查所有连续子串
    # 如果任一单个数字是3的倍数
    if int(s[0]) % 3 == 0 or int(s[1]) % 3 == 0:
        return True
    # 检查整体两位数
    if int(s) % 3 == 0:
        return True
    # 否则不幸运
    return False

def count_lucky(L: int, R: int) -> int:
    count = 0
    # 对于小于100的数，逐个判断
    for num in range(L, min(R, 99) + 1):
        if is_lucky(num):
            count += 1
    # 对于大于等于100的部分，全部都是幸运数
    if R >= 100:
        low = max(L, 100)
        count += (R - low + 1)
    return count

# 示例：
L, R = 8, 19
print(count_lucky(L, R))
