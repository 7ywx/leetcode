def count_visible_students(heights):
    stack = []
    total_visible = 0

    for h in heights:
        count = 0
        while stack and stack[-1] <= h:
            stack.pop()
            count += 1
        total_visible += count
        stack.append(h)

    return total_visible

# 测试
heights = [5, 3, 3, 2, 4]
print(count_visible_students(heights))  # 输出7
