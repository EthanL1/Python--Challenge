import os
import csv
import decimal

#make in and out filepaths to be uses
doc = open("Answer/voting_results.txt","w")
data_1 = os.path.join("Data","election_data_2.csv")

total_votes = 0
region = []

#used to calculate how many rows are present in the doc. Giving us the number of votes
with open(data_1, 'r') as csv_file:
    dataFile =  csv.reader(csv_file, delimiter=',')

    #skips the first header
    next(dataFile, None)    
    
    for row in dataFile:
        if row[0] == None:
         break
        else:
            total_votes += 1
#writing  total amount of votes to the output file
doc.write("\n")
doc.write("Election Results"+"\n")
doc.write("----------------------------------\n")
doc.write ('Total votes: ' + str(total_votes)+"\n")
doc.write("----------------------------------\n")

#writing  total amount of votes to the terminal
print("\n")
print("Election Results")
print("----------------------------------")
print ('Total votes: ' + str(total_votes))
print("----------------------------------")

#intiate the voting dictonary with key being candiate and value being the total number of votes they got
voting_dict= {}

with open(data_1, 'r') as csv_file:
    dataFile =  csv.reader(csv_file, delimiter=',')
    
    next(dataFile, None)
    
    for row in dataFile:
        #checks the third element of the file which is the candidate column
        #adds candiadtes name to the dictionary if not key is present with their name
        if row[2]   not in voting_dict:
            voting_dict[row[2]] = 1
        else:
            #adds the matching candidates by one value to get count of their votes
            voting_dict[row[2]] =  voting_dict[row[2]] + 1 
    
           
    
    for key, value in voting_dict.items():
        vote_percentage = round((value)/(total_votes)*100,2)
        doc.write(key + ": " + str(vote_percentage)+"% " + " (" + str(value) + ")\n")
        print(key + ": " + str(vote_percentage)+"% " + " (" + str(value) + ")")
doc.write("----------------------------------\n")
print("----------------------------------")
winner = max(voting_dict, key=voting_dict.get)
doc.write("Your winner is: "+ winner + "\n")
print("Your winner is: "+ winner + "\n")
doc.close()