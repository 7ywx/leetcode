import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee_name = []
    employee_id = employee['id'].tolist()
    for row in employee.itertuples():
        if not pd.isna(row.managerId) and row.managerId in employee_id:
            if row.salary > employee.loc[row.managerId==employee.id, 'salary'].values[0]:
                employee_name.append(row.name)
    return pd.DataFrame(employee_name, columns=['Employee'])

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # 首先，我们使用布尔型索引找到所有非空managerId且managerId存在于employee.id中的行
    manager_condition = ~pd.isna(employee['managerId']) & employee['managerId'].isin(employee['id'])
    # 接下来，我们通过比较薪水来筛选
    salary_condition = employee['salary'] > employee.loc[.managerId==employee.id, 'salary'].values[0]
    # 最后，我们获取名字列
    employee_name = employee[manager_condition & salary_condition]['name']
    return pd.DataFrame(employee_name, columns=['Employee'])

data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}
data1 = {
    'id': [1, 3, 2],
    'name': ['Mark', 'Jack', 'Alan'],
    'salary': [40000, 30000, 20000],
    'managerId': [3, 2, None]
}
employee = pd.DataFrame({
    'id': [1, 2],
    'name': ['Mark', 'Jack'],
    'salary': [30000, 20000],
    'managerId': [2, pd.NaT]
})
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
# employee_id = employee['id'].tolist()
# print(employee_id)
print(find_employees(df))
