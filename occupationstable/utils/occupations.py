import random

def scanCSV(CSVfile):   # imports specified csv file and assigns its contents a variable
    instream = open(CSVfile, 'r')
    content = instream.read().strip()
    instream.close()
    return content

def genDictionary(data):
    lines = data.split("\n")
    jobDict = {}
    del lines[0]
    del lines[-1]
    for line in lines:
        entry = line.rsplit(",", 2)
        entry[1] = float(entry[1])
        value = [entry[1], entry[2]]
        jobDict[entry[0]] = value
    return jobDict

def genList(data):
    lines = data.split("\n")
    jobList = []
    for line in lines:
        entry = line.rsplit(",", 2)
        jobList.append(entry)
    return jobList

def getRandomOccupation(occupations):
    # print occupations
    occupationNames = []
    for occupation in occupations:
        # pos = 0
        for i in range(int(occupations[occupation][0] * 10)):
            # pos += 1
            occupationNames.insert(len(occupationNames), occupation)
        # print pos
    random.shuffle(occupationNames)
    # print occupationNames
    return occupationNames[random.randint(0, len(occupationNames) - 1)]

def listOccupation():
    return genList(scanCSV("data/occupations.csv"))

def findOccupation():
    occupationDict = genDictionary(scanCSV("data/occupations.csv"))
    occupation = getRandomOccupation(occupationDict)
    link = occupationDict[occupation][1]
    info = [occupation, link]
    return info

