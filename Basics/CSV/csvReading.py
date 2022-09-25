import pandas as pd

df = pd.read_csv('Basics/CSV/student_csv_file.csv')
print(df.to_string()) #Gets the data from csv in string
print(type(df.to_string())) #without to String it'll give a pd object
print(df.head(1).to_string()) #head splices the number of rows
print(df['name']) #Calling speicifc column
print (df.columns) #Calling all columns

print(df.iloc[1]) #selecting specific row

studentOtherData = {'course': ['BSSE','BSCS']}

studentFullData = df.join(pd.DataFrame(studentOtherData)) #Since df is a dataframe object we need to convert our dictionary to dataframe as well
print(studentFullData)

print(studentFullData.to_html('HTML_Student')) #Converts whole CSV to HTML file