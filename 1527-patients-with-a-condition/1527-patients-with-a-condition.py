import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.split(" ").apply(
    lambda words: any(word.startswith('DIAB1') for word in words)
)]