import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee=employee.drop_duplicates('salary')
    if len(employee)>=2:
        return pd.DataFrame(employee.salary.nlargest(2).tail(1).rename('SecondHighestSalary'))
    else:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    