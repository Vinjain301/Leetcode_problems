import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered_customer_ids=orders['customerId']
    return customers.query('id not in @ ordered_customer_ids')[['name']].rename(columns={'name':'Customers'})
    