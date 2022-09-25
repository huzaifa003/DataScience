import csv



file = open('Basics/CSV/student_csv_file.csv', 'w', newline='')
csvWriter = csv.writer(file)

header = ['name','id','semester','gpa','contact']
data =[
    ['xyz','1','4','3.0','0321456789'],
    ['abc','1','4','2.0','0321442489'],
]

csvWriter.writerow(header)
csvWriter.writerows(data)
file.close()