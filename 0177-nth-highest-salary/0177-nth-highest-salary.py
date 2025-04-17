import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee=employee.drop_duplicates('salary')
    if len(employee)>=N and N>0:
        return pd.DataFrame(employee.salary.nlargest(N).tail(1).rename(f"getNthHighestSalary({N})"))
    else: return pd.DataFrame({f"getNthHighestSalary({N})":[None]})