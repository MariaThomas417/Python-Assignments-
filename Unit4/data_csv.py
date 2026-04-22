import csv

row_count=0
with open('\Users\maria\OneDrive\Documents',"r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        row_count +=1

print("total no. of rows: ", row_count)
