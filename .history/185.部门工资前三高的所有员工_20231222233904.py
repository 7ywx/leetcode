import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """
    返回DataFrame中第N高的工资值

    参数：
    employee: 包含员工信息的DataFrame，其中包含'salary'列
    N: 第N高的工资值的索引

    返回值：
    包含第N高的工资值的DataFrame，如果找不到则返回None
    """
    # 将salary列中的工资值去重并存储在t中
    t = list(set(employee['Salary']))
    # 对t进行排序
    t.sort()
    # 如果 N 小于等于 0
    if N <= 0:
        # 返回一个包含一个含有 pd.NA 元素的 DataFrame，列名为 f'getNthHighestSalary({N})'
        return None
    # 如果t的长度小于N，返回None
    if len(t) < N:
        ans = None
    else:
        # 否则返回去重排序后的第N个值
        ans = t[-N]
    # 返回一个包含单行的DataFrame，该行的列名为[f'getNthHighestSalary({N})']
    return ans

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    e_d = Employee.merge(Department, left_on='departmentId', right_on='id', how='inner').rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
    # e_d = e_d.groupby('Department')['Salary'].sort_values(by='Salary')
    # 如果你想要对每个部门的薪资按降序排序，可以添加`ascending=False`参数：
    e_d = e_d.groupby('Department').apply(lambda x: x.sort_values(by='Salary', ascending=False))
    IT_3th_salaries = nth_highest_salary(e_d[e_d['Department'] == 'IT'], 3)
    Sales_3th_salaries = nth_highest_salary(e_d[e_d['Department'] == 'Sales'], 3)
    print(IT_3th_salaries)
    print(e_d)





# Create the Employee table
Employee = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['Joe', 'Henry', 'Sam', 'Max', 'Janet', 'Randy', 'Will'],
    'salary': [85000, 80000, 60000, 90000, 69000, 85000, 70000],
    'departmentId': [1, 2, 2, 1, 1, 1, 1]
})

# Create the Department table
Department = pd.DataFrame({
    'id': [1, 2],
    'name': ['IT', 'Sales']
})
top_three_salaries(Employee, Department)
