# chose this method because it does not hold any set of information in arrays
# or lists. It reads the list once while doing all the calculations without 
# holding large sets of information. In the case of BIG data, it can work smoothly

import os
import csv

path = os.path.join('budget_data_1.csv')

#opening the file to read the starting revenue, then ending the for loop.
#goal for this is to just get starting revenue used for calculations next
with open(path, newline='') as lookup:
    reader = csv.reader(lookup)
    next(reader)
    for x in reader:
        startrev = int(x[1])
        break

# this is where the real chunk begins. stating the variables now. Setting
# the rev to the startnumb calculated 
rev = startrev
revsum = 0
changesum = 0
maxchange = 0
minchange = 0

with open(path, newline='') as lookup:
    reader = csv.reader(lookup)
    next(reader)
    
    # doing an enumerate so that it creates a counter(i) to count #rows
    # keep in mind enumerate starts at 0
    for i, x in enumerate(reader):
        
        change = int(x[1]) - rev #for the first iteration it should be zero, hence startrev
        if change>maxchange:
            maxchange = change
            maxmon = x[0]
        if change<minchange:
            minchange = change
            minmon = x[0]

        rev = int(x[1])

        revsum += rev
        changesum += change

    # dividing by i because i is one less than total number of months and so should
    # the array be for change since first month has no change    
    avg = (changesum)/(i)

print("\nFinancial Analysis \n------------------------")
print(f'Total Months: {i+1}')
print(f'Total Revenue: ${revsum}')
print(f'Average Revenue Change: ${round(avg,2)}')
print(f'Greatest Increase in Rev: {maxmon}, ${maxchange}')
print(f'Greatest Decrease in Rev: {minmon}, ${minchange}\n')
