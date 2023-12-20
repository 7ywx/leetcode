import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee_name = []
            employee_id = employee['id'].tolist()
    for row in employee.itertuples():
        if not pd.isna(row.managerId) and row.managerId in employee_id:
            if row.salary > employee.loc[row.managerId==employee.id, 'salary'].values[0]:
                employee_name.append(row.name)
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
print(find_employees(employee))
