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
        return 0
    # 如果t的长度小于N，返回None
    if len(t) < N:
        ans = 0
    else:
        # 否则返回去重排序后的第N个值
        ans = t[-N]
    # 返回一个包含单行的DataFrame，该行的列名为[f'getNthHighestSalary({N})']
    return ans

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    e_d = employee.merge(department, left_on='departmentId', right_on='id', how='inner').rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
    # print(e_d)
    # print(department)
    _3th = {}
    for name in department['name']:
        _3th[name] = nth_highest_salary(e_d[e_d['Department'] == name], 3)
    print(_3th)
    # IT_3th_salaries = nth_highest_salary(e_d[e_d['Department'] == 'IT'], 3)
    # Sales_3th_salaries = nth_highest_salary(e_d[e_d['Department'] == 'Sales'], 3)
    conditions = pd.DataFrame()
    for name, salarys in _3th.items():
        condition = e_d[(e_d['Department'] == name) & (e_d['Salary'] >= salarys)]
        print(condition)
    #result = e_d[((e_d['Department'] == 'IT') & (e_d['Salary'] >= IT_3th_salaries)) | ((e_d['Department'] == 'Sales') & (e_d['Salary'] >= Sales_3th_salaries))][["Department","Employee","Salary"]]
    # print(result)
    # return result





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
data = {
    'id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['Joe', 'Henry', 'Sam', 'Max', 'Janet', 'Randy', 'Will'],
    'salary': [85000, 80000, 60000, 90000, 69000, 85000, 70000],
    'departmentId': [1, 2, 2, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

data1 = [
    {'id': 1, 'name': 'Joe', 'salary': 60000, 'departmentId': 1},
    {'id': 4, 'name': 'Max', 'salary': 60000, 'departmentId': 2}
]

df1 = pd.DataFrame(data1)

data3 = [
    {'id': 1, 'name': 'IT'},
    {'id': 2, 'name': 'HR'}
]

df3 = pd.DataFrame(data3, columns=['id', 'name'])

top_three_salaries(df1, df3)
