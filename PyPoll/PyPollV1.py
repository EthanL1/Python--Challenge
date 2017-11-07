import os
import csv
import decimal
"""
## Option 2: PyPoll

![Vote-Counting](Images/Vote_counting.jpg)

In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

As an example, your analysis should look similar to the one below:
"""

'''
Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
```
'''

''' purpose of this code is to calculate voting data and notfiy the user which candidates got which votes and what portions of the votes.'''


data_1 = os.path.join("Data","election_data_2.csv")
total_votes = 0
region = []
with open(data_1, 'r') as csv_file:
    dataFile =  csv.reader(csv_file, delimiter=',')

    next(dataFile, None)    
    for row in dataFile:
        if row[0] == None:
         break
        else:
            total_votes += 1
print ('Total votes: ' + str(total_votes))
marsh_votes = 0
queen_votes = 0
bamoo_votes = 0 
trandee_votes = 0
with open(data_1, 'r') as csv_file:
    dataFile =  csv.reader(csv_file, delimiter=',')

    for row in dataFile:
        if row[1] == "Marsh":
            marsh_votes +=1
        elif row[1] == "Queen":
            queen_votes +=1
        elif row[1] == "Bamoo":
            bamoo_votes +=1    
        else:
            trandee_votes += 1
    print(marsh_votes)
    print(queen_votes)
    print(bamoo_votes) 
    print(trandee_votes)

marsh_percentage = ((marsh_votes/total_votes)*100)
queen_percentage = ((queen_votes/total_votes)*100)
bamoo_percentage = ((bamoo_votes/total_votes)*100)
trandee_percentage = ((trandee_votes/total_votes)*100)

print("-----------")
print("total number of votes is: " + str(total_votes) )
print("---------")
print("Marsh: " + str(round(marsh_percentage,2))+"%     "+ "("+ str(marsh_votes)+")")

if marsh_percentage > queen_percentage and marsh_percentage > bamoo_percentage and marsh_percentage > trandee_percentage
