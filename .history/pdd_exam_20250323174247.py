def count_lucky_numbers(L, R):
    # Precompute lucky numbers for numbers up to 999
    max_num = 999
    lucky = [False] * (max_num + 1)
    for x in range(max_num + 1):
        s = str(x)
        if '0' in s:
            lucky[x] = True
            continue
        n = len(s)
        found = False
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += int(s[j])
                if total % 3 == 0:
                    found = True
                    break
            if found:
                break
        lucky[x] = found

    # Build prefix sum array
    prefix = [0] * (max_num + 2)  # prefix[i] = count of lucky numbers < i
    for i in range(1, max_num + 2):
        prefix[i] = prefix[i-1] + (1 if (i-1 <= max_num and lucky[i-1]) else 0)

    # Calculate count_ge4: numbers >= 1000 in [L, R]
    lower_ge4 = max(L, 1000)
    if lower_ge4 > R:
        count_ge4 = 0
    else:
        count_ge4 = R - lower_ge4 + 1

    # Calculate count_le3_lucky: numbers <= 999 in [L, R]
    lower_le3 = max(L, 0)
    upper_le3 = min(R, 999)
    if lower_le3 > upper_le3:
        count_le3 = 0
    else:
        # prefix[upper_le3 + 1] is sum from 0 to upper_le3 inclusive
        # prefix[lower_le3] is sum from 0 to lower_le3 - 1
        count_le3 = prefix[upper_le3 + 1] - prefix[lower_le3]

    return count_ge4 + count_le3

# 示例输入
L = 8
R = 19
print(count_lucky_numbers(L, R))  # 输出应为1
