import pandas as pd

# def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
#     employee_name = []
#     for row in employee.itertuples():
#         employee_id = employee['id'].tolist()
#         if not pd.isna(row.managerId) and row.managerId in employee_id:
#             if row.salary > employee.loc[row.managerId==employee.id, 'salary'].values[0]:
#                 employee_name.append(row.name)
#     return pd.DataFrame(employee_name, columns=['Employee'])

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # 通过 dropna 来过滤掉 managerId 缺失的行
    employee = employee.dropna(subset=['managerId'])

    # 使用 apply 函数来应用条件和向量化操作
    employees_above_manager = employee[employee['salary'] > employee['salary'].loc[employee['managerId'].isin(employee['id'])].values]

    # 使用 boolean 索引获取名字
    employee_name = employees_above_manager[employees_above_manager['salary'] > employees_above_manager['salary'].loc[employees_above_manager['managerId'].isin(employees_above_manager['id'])]].index.tolist()

    # 返回结果，直接使用 index 列而不是创建一个单独的 Employee 列
    return employee.loc[employee_name]

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
print(find_employees(employee))
