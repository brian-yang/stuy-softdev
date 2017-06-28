import random

def scanCSV(CSVfile):   # imports specified csv file and assigns its contents a variable
    instream=open(CSVfile, 'r')
    content=instream.read().strip()
    instream.close()
    return content

def genDictionary(data):
    list1 = data.split("\n")
    list2 = []
    dict1 = {}
    del list1[0]
    del list1[-1]
    for x in list1:
        entry = x.rsplit(",", 1)
        entry[1] = float(entry[1])
        list2.append(entry)
    for a in list2:
        dict1[a[0]] = a[1]
    return dict1

def getRandomOccupation(occupations):
    # print occupations
    occupationNames = []
    for occupation in occupations:
        # pos = 0
        for i in range(int(occupations[occupation] * 10)):
            # pos += 1
            occupationNames.insert(len(occupationNames), occupation)
        # print pos
    random.shuffle(occupationNames)
    # print occupationNames
    return occupationNames[random.randint(0, len(occupationNames) - 1)]

print getRandomOccupation(genDictionary(scanCSV("occupations.csv")))
#print scanCSV("occupations.csv")
