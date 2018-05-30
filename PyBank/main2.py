import os
import csv

path = os.path.join('budget_data_1.csv')

date = []
rev = []
change = []


with open(path, newline='') as lookup:
    reader = csv.reader(lookup)
    next(reader)
    
    for i, x in enumerate(reader):
          
        date.append(x[0])
        rev.append(int(x[1]))

    months = len(date)
    for x in range(months-1):
        diff = rev[x+1] - rev[x]
        change.append(diff)
        
Sum = sum(rev)
avgchange = sum(change)/len(change)
maxchange = max([(Max,i) for i, Max in enumerate(change,1)])
minchange = min([(Min,i) for i, Min in enumerate(change,1)])

print(months)
print(Sum)    
print(avgchange)
print(f'{date[maxchange[1]]} ({maxchange[0]})')
print(f'{date[minchange[1]]} ({minchange[0]})')