import csv

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)

print d
for k in d:
    print k
    #Q: What can you print here to make each line show only
    #   a name and its ID?
    #   eg,
    #   sasha, 3

    
fObj = open("courses.csv") 
d=csv.DictReader(fObj)

for k in d:
    print k
