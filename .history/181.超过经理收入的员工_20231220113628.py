import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # 初始化一个空列表来存储员工姓名
    employee_name = []
    # 从员工数据中提取出员工id列表
    employee_id = employee['id'].tolist()
    # 遍历员工数据的每一行
    for row in employee.itertuples():
        # 如果员工的managerId不为空且在员工id列表中
        if not pd.isna(row.managerId) and row.managerId in employee_id:
            # 如果员工的薪水大于其经理的薪水
            if row.salary > employee.loc[row.managerId==employee.id, 'salary'].values[0]:
                # 将员工姓名添加到员工姓名列表中
                employee_name.append(row.name)
    # 返回含有"Employee"列的员工姓名数据帧
    return pd.DataFrame(employee_name, columns=['Employee'])

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    data1 = pd.merge(employee,employee,right_on = 'id',left_on = 'managerId',how='inner')
    data2 = data1[data1['salary_x']>data1['salary_y']]
    data3 = data2[['name_x']].rename(columns={'name_x':'Employee'})
    return data3[['Employee']]

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
