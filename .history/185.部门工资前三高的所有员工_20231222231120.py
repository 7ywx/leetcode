import pandas as pd
def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    e_d = Employee.merge(Department, left_on='departmentId', right_on='id', how='inner')

    # Group the merged table by departmentId and name_y, then transform the salary column to get the maximum salary for each department
    e_d['max_salary'] = e_d.groupby(['departmentId', 'name_y'])['salary'].transform('max')

    # Filter the merged table to only include rows where salary is equal to max_salary, then rename the name_y column to Department and the name_x column to Employee
    department_highest_salary = e_d[e_d['salary'] == e_d['max_salary']].rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})

    # Select only the Department, Employee, and Salary columns from the filtered table
    department_highest_salary = department_highest_salary[['Department', 'Employee', 'Salary']]

    # Return the department_highest_salary table
    print(department_highest_salary)
    return department_highest_salary

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
