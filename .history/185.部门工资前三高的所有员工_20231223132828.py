import pandas as pd
# from scipy.stats import scoreatpercentile
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """
    计算第N高的薪水。

    参数：
    employee: 包含员工薪水信息的DataFrame
    N: 前N高的薪水的排序，如N=1表示最高薪水，N=2表示次高薪水等

    返回值：
    返回第N高的薪水，如果N小于等于0，返回0

    """
    t = list(set(employee['Salary']))
    t.sort()
    if N <= 0:
        return 0
    if len(t) < N:
        ans = 0
    else:
        ans = t[-N]
    return ans

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    计算每个部门的第三高薪水。

    参数：
    employee: 包含员工信息的DataFrame，包括员工编号、姓名和所在部门编号。
    department: 包含部门信息的DataFrame，包括部门编号和部门名称。

    返回：
    一个包含每个部门的第三高薪水员工信息的DataFrame。

    """
    # 合并员工和部门信息，并重命名列名
    e_d = employee.merge(department, left_on='departmentId', right_on='id', how='inner').rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})

    # 存储每个部门的第三高薪水
    _3th = {}
    for name in department['name']:
        _3th[name] = nth_highest_salary(e_d[e_d['Department'] == name], 3)
        # _3th[name] = scoreatpercentile(e_d[e_d['Department'] == name]['Salary'], 97)

    # 创建存储条件的DataFrame
    conditions = pd.DataFrame(columns=['Department','Employee','Salary'])

    # 将每个部门的第三高薪水条件下的员工信息添加到conditions中
    for name, salarys in _3th.items():
        condition = e_d[(e_d['Department'] == name) & (e_d['Salary'] >= salarys)][["Department","Employee","Salary"]]
        conditions = pd.concat([conditions, condition])

    # 返回conditions
    return conditions

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 使用left_on和right_on参数将employee和department数据框按照"departmentId"和'id'列进行左连接
    merge_df = pd.merge(employee, department, left_on="departmentId", right_on='id', how='left')

    # 将连接后的数据框的列名进行重命名，包括'name_x'变为'Employee'，'name_y'变为'Department'，'salary'变为'Salary'
    merge_df.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'}, inplace=True)

    # 对连接后的数据框按照'Department'列分组，根据'Salary'列进行排名，采用密集法（method='dense'），从大到小排序（ascending=False）
    merge_df['rank'] = merge_df.groupby('Department')['Salary'].rank(method='dense', ascending=False)

    # 保留排名前3的记录
    merge_df = merge_df[merge_df['rank'] <= 3]

    # 返回包含'Department'、'Employee'和'Salary'列的数据框
    print(merge_df)
    return merge_df[['Department', 'Employee', 'Salary']]



# 创建Employee表格
Employee = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['Joe', 'Henry', 'Sam', 'Max', 'Janet', 'Randy', 'Will'],
    'salary': [85000, 80000, 60000, 90000, 69000, 85000, 70000],
    'departmentId': [1, 2, 2, 1, 1, 1, 1]
})

# 创建Department表格
Department = pd.DataFrame({
    'id': [1, 2],
    'name': ['IT', 'Sales']
})

test1E = pd.DataFrame([
    {'id': 1, 'name': 'Joe', 'salary': 60000, 'departmentId': 1},
    {'id': 4, 'name': 'Max', 'salary': 60000, 'departmentId': 2}
])
test1D = pd.DataFrame([
    {'id': 1, 'name': 'IT'},
    {'id': 2, 'name': 'HR' }
])
df4 = pd.DataFrame({ 'id': [], 'name': [], 'salary': [], 'departmentId': [] })
df5 = pd.DataFrame({'id': [], 'name': []})
top_three_salaries(test1E, test1D)
