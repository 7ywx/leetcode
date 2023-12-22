import pandas as pd
def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    e_d = Employee.merge(Department, left_on='departmentId', right_on='id', how='inner')
    e_d = e_d.sort_values(by='salary', ascending=False)
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
