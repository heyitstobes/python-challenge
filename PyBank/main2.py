import os 
import csv 

months = 0
total = 0 
lesser = 0
greater = 0

csvpath=os.path.join('PyBank','homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader: 
        months += 1
        total += int(row[1])
        if greater < int(row[1]):
            greater = int(row[1])
            great_mo = row[0]
        elif lesser > int(row[1]):
            lesser = int(row[1])
            less_mo = row[0]





str1="Financial Analysis"+ "\n" + "----------------------------" + "\n" + "Total Months: " + str(months) + "\n" + "Total: "+ str(total) + "\n" + "Average Change: " + str(round((total/months),2)) + "\n" + "Greatest Increase in Profits: " + str(great_mo) + ": " + str(greater) + "\n" + "Greatest Decrease in Profits: " + str(less_mo) + ": " + str(lesser)

print(str1)


f = open("output_file.txt","w+")
f.write(str1)
f.close()