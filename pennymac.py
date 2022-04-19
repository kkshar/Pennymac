# store each line of the file as an element in a list
def getData(file):
    f = open(file)
    lst = []
    for line in f:
        lst += [line.split()]
    return lst

# converts strings to float
def convertStr(colA, colB, func=lambda x: x):
    for i in range(len(colA)):
        colA[i] = float(func(colA[i]))
        colB[i] = float(func(colB[i]))

# Take the absolute difference between two columns, sort the difference, and return the least one
def leastDiffItem(itemCol, colA, colB):
    difference = [[item, abs(a - b)] for item, a, b in zip(itemCol, colA, colB)]
    sorted_diff = sorted(difference, key=lambda x: x[1])
    return sorted_diff[0][0]


def weatherData():
    lst = getData('w_data.dat')

    # clean and get data for needed column
    data = lst[6:37]
    day = [x[0] for x in data]
    maxT = [x[1] for x in data]
    minT = [x[2] for x in data]

    # convert minT and maxT to float
    convertStr(maxT, minT, lambda x: x.replace('*', ''))

    # output result
    print('Smallest temperature spread is on day', leastDiffItem(day, maxT, minT))


def soccerData():
    soccer = getData('soccer.dat')

    # clean and get data for needed column
    soccer_data = soccer[3: 20] + soccer[21:24]
    team = [x[1] for x in soccer_data]
    for_goals = [x[6] for x in soccer_data]
    against_goals = [x[8] for x in soccer_data]

    # convert F and A to float
    convertStr(for_goals, against_goals)

    # output result
    print('The team with the smallest difference in ‘for’ and ‘against’ goals is', leastDiffItem(team, for_goals, against_goals))

weatherData()
soccerData()