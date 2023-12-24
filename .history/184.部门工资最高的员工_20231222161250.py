import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:




# Create the DataFrame for Employee table
employee_df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
})

# Create the DataFrame for Department table
department_df = pd.DataFrame({
    'id': [1, 2],
    'name': ['IT', 'Sales']
})
