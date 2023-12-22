import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    coustomers_orders = customers.merge(orders, on='customerId', how='left')
    print(coustomers_orders)
# Customers table
customers = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
}
df_customers = pd.DataFrame(customers)

# Orders table
orders = {
    'id': [1, 2],
    'customerId': [3, 1]
}
df_orders = pd.DataFrame(orders)

find_customers(df_customers, df_orders)
