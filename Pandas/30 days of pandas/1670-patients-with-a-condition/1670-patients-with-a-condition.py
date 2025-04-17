import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients.conditions.str.split().map(lambda x: any(item.startswith('DIAB1') for item in x))]
    