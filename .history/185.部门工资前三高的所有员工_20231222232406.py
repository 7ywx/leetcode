import pandas as pd
def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    e_d = Employee.merge(Department, left_on='departmentId', right_on='id', how='inner').rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
    # e_d = e_d.groupby('Department')['Salary'].sort_values(by='Salary')
    # 如果你想要对每个部门的薪资按降序排序，可以添加`ascending=False`参数：
    e_d = e_d.groupby('Department').apply(lambda x: x.sort_values(by='Salary', ascending=False))
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
