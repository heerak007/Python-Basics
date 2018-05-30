import os
import csv

path = os.path.join('election_data_1.csv')
candidates = []
count = []

with open(path, newline='') as lookup:
    reader = csv.DictReader(lookup)
    for x in reader:

        cand = x["Candidate"]
        if cand not in candidates:
            candidates.append(cand)
            count.append(0)
            
        count[candidates.index(cand)] +=1
        
total = sum(count)
winner = count.index(max(count))
print("\nElection Results \n------------------------")
print(f"Total Votes: {total} \n------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {'{:.1%}'.format(float(count[i]/total))}  ({count[i]})")
print(f"------------------------\nWinner is: {candidates[winner]}\n")