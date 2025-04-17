import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
   return pd.DataFrame(accounts.assign(category=pd.cut(accounts.income, bins=[0, 20000, 50001, float('inf')], labels=['Low Salary', 'Average Salary', 'High Salary'], right=False)).rename(columns={'account_id': 'accounts_count'}).groupby('category')['accounts_count'].nunique().reset_index())
    