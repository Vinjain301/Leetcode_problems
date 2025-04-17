import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank1']=employee.groupby('departmentId')['salary'].rank(method='dense',ascending=False)
    return pd.merge(employee[employee.rank1==1],department,how='inner',left_on='departmentId',right_on='id')[['name_y','name_x',  'salary' ]].rename(columns={'name_x':'Employee',  'salary':'Salary' ,'name_y':'Department'})
    