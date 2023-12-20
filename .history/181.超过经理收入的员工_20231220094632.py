import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee_name = []
    for index,row in employee.itertuples():
        if row.salary > employee[employee['id'] == row.manager_Id]['salary']:
            employee_name.append(row.name)
    return pd.DataFrame(employee_name, columns=['Employee'])


data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}

df = pd.DataFrame(data)
print(find_employees(df))
