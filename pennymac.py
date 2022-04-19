# split each line of string into a list where each word is a list item.
def getData(file):
    f = open(file)
    lst = []
    for line in f:
        lst += [line.split()]
    return lst

# return the specified column of data
def getColumnData(data, columnIndex):
    return [x[columnIndex] for x in data]

# convert a column of strings to floats, a function can be passed in to clean the string first (default is identity).
def convertStr(colA, func=lambda x: x):
    for i in range(len(colA)):
        colA[i] = float(func(colA[i]))

# Take the absolute difference between two columns, sort the difference, and return the least one
def leastDiffItem(itemCol, colA, colB):
    difference = [[item, abs(a - b)] for item, a, b in zip(itemCol, colA, colB)]
    sorted_diff = sorted(difference, key=lambda x: x[1])
    return sorted_diff[0][0]



def weatherData():
    lst = getData('w_data.dat')
    start_row = 6
    end_row = 37

    # clean and get data for needed column
    data = lst[start_row:end_row]
    day = getColumnData(data, 0)
    maxT = getColumnData(data, 1)
    minT = getColumnData(data, 2)

    # convert minT and maxT to float; there are '*' in some entries, use a function to clean that
    convertStr(maxT, lambda x: x.replace('*', ''))
    convertStr(minT, lambda x: x.replace('*', ''))

    # output result
    print('Smallest temperature spread is on day', leastDiffItem(day, maxT, minT))


def soccerData():
    soccer = getData('soccer.dat')
    start_row = 3
    end_row = 24

    # clean and get data for needed column
    data = soccer[start_row: 20] + soccer[21:end_row] # there is a dashed line on line 20
    team = getColumnData(data, 1)
    for_goals = getColumnData(data, 6)
    against_goals = getColumnData(data, 8)

    # convert F and A to float
    convertStr(for_goals)
    convertStr(against_goals)

    # output result
    print('The team with the smallest difference in ‘for’ and ‘against’ goals is', leastDiffItem(team, for_goals, against_goals))

weatherData()
soccerData()