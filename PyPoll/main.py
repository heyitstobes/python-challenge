import os 
import csv 

khan = 0
correy = 0 
li = 0
otooley = 0
total=0

csvpath=os.path.join('PyPoll','homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader: 
        total += 1
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1 
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1

if khan > li: 
    if khan > correy:
        if khan > otooley:  
            winner = "Khan"

if li > khan: 
    if li > correy:
        if li > otooley:  
            winner = "Li"

if correy > khan: 
    if correy > li:
        if correy > otooley:  
            winner = "Correy"

if otooley > khan: 
    if otooley > li:
        if otooley > correy:  
            winner = "O'Tooley"



open_str = ("Election Results" + "\n" + "-------------------------" + "\n" + "Total Votes: " + str(total) + "\n" + "-------------------------" + "\n")
khan_str =("Khan: " + str(round(((khan/total)*100),3)) + "%" + " (" +str(khan)+ ")" + "\n")
correy_str =("Correy: " + str(round(((correy/total)*100),3)) + "%" + " (" +str(correy)+ ")" + "\n")
li_str =("Li: " + str(round(((li/total)*100),3)) + "%" + " (" +str(li)+ ")" + "\n")
otooley_str =("O'tooley: " + str(round(((otooley/total)*100),3)) + "%" + " (" +str(otooley)+ ")" + "\n")
winner = ("-------------------------" + "\n" + "Winner: " + winner + "\n" + "-------------------------")

final_str = (open_str + khan_str + correy_str + li_str + otooley_str + winner)

print(final_str)

f = open("final_text_file.txt","w+")
f.write(final_str)
f.close()