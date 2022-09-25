import pandas as pd

df = pd.read_csv('Basics/CSV/student_csv_file.csv')
print(type(df.to_string()))
print(df.head().to_string())