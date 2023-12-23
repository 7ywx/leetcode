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
    merge_df = pd.merge(employee, department, left_on="departmentId", right_on='id', how='left')
    merge_df.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'}, inplace=True)
    merge_df['rank'] = merge_df.groupby('Department')['Salary'].rank(method='dense', ascending=False)
    merge_df = merge_df[merge_df['rank'] <= 3]
    return merge_df[['Department', 'Employee', 'Salary']]



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
df4 = pd.DataFrame({ 'id': [], 'name': [], 'salary': [], 'departmentId': [] })
df5 = pd.DataFrame({'id': [], 'name': []})
top_three_salaries(Employee, Department)
