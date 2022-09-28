import csv

def removeNullRows(df):
    result = []
    for row in df:
        if '' not in row:
            result.append(row)
    return result

def getMean(col):
    summation = 0
    count = 0
    for x in col:
        if x != '':
            summation += float(x)
            count += 1
    return round(summation/count, 1)

def transform(result):
    rows = []
    for row in zip(*result):
        rows.append(row)
    return rows

def fillNullWithMean(df):
    result = []
    for col in zip(*df):
        mean = getMean(col)
        col1 = [mean if x == '' else x for x in col]
        result.append(col1)

def fillNullWithInterpolation(df):
    result = []
    for col in zip(*df):
        length = len(col)
        col = list(col)
        for x in range(0, length):
            if col[x] == '':
                if x == 0:
                    col[x] = 0 if length == 1 else col[x + 1]
                elif x == (length - 1):
                    col[x] = col[x -1]
                else:
                    col[x] = round((float(col[x - 1]) + float(col[x + 1])) / 2, 2)
        result.append(col)
    
    return transform (result)

def fillNullWithConstant(df, constant = 0):
    result = []
    for row in df:
        row1 = [constant if x == '' else x for x in row]
        result.append(row1)
    return result

def writeFile(result):
	with open('output.csv', 'w') as output_file:
		csvwriter = csv.writer(output_file) 

		csvwriter.writerows(result)

def processChoice(choice, df):
	if choice == 1:
		return removeNullRows(df)
	elif choice == 2:
		return fillNullWithMean(df)
	elif choice == 3:
		return fillNullWithInterpolation(df)
	elif choice == 4:
		return fillNullWithInterpolation(df)

def readFile(filename):
	inputFile = open(filename, 'r')
	df = csv.reader(inputFile)
	return df, inputFile

def main(choice):
	df, inputFile = readFile('data.csv')
	header = next(df)

	result = processChoice(choice, df)
	result.insert(0, header)

	writeFile(result)
	inputFile.close()

main(3) #<--Insert Method Number

#List of Methods:
#1. Remove rows with missing data
#2. Fill by column average (mean)
#3. Fill by linear interpolation
#4. Fill by global constant


ll