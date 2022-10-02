#This is a program that will accept & read a .csv file.
#The .csv file must be in the same folder as this program.
#This program will accept the request of the user to remove the rows with missing data, fill by column average (mean), fill by linear interpolation, and fill by global constant.
#The output will be a .csv file of the user's request.

#Made by Ellyza Mari Jocson Papas
#Subject: Compsci 35 - A: Data Mining

import csv

def removeNullRows(data):
	result = []
	for row in data:
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
	return round(summation/count, 2)

def transform(result):
	rows = []
	for row in zip(*result):
		rows.append(row)
	return rows

def fillNullWithMean(data):
	result = []
	for col in zip(*data):
		mean = getMean(col)
		col1 = [mean if x == '' else x for x in col]
		result.append(col1)

	return transform(result)

def fillNullWithInterpolation(data):
	result = []
	for col in zip(*data):
		length = len(col)
		col = list(col)
		for x in range(0, length):
			if col[x] == '':
				if x == 0:
					col[x] = 0 if length==1 else col[x+1]
				elif x == (length-1):
					col[x] = col[x-1]
				else:
					col[x] = round((float(col[x-1]) + float(col[x+1]))/2, 2)
		result.append(col)

	return transform(result)

def fillNullWithConstant(data, constant = 0):
	result = []
	for row in data:
		row1 = [constant if x == '' else x for x in row]
		result.append(row1)
	return result

def writeToFile(result):
	with open('output.csv', 'w') as output_file:
		# creating a csv writer object 
		csvwriter = csv.writer(output_file) 

		# writing the result rows 
		csvwriter.writerows(result)

def processChoice(choice, data):
	if choice == 1:
		return removeNullRows(data)
	elif choice == 2:
		return fillNullWithMean(data)
	elif choice == 3:
		return fillNullWithInterpolation(data)
	elif choice == 4:
		return fillNullWithConstant(data)

def read_file(filename):
	input_file = open(filename, 'r')
	data = csv.reader(input_file)
	return data, input_file

try:
	output = "output.csv"
	selection = int(input("METHODS:\n"
                          "1. Remove rows with missing data.\n"
                          "2. Fill by column average (mean)\n"
                          "3. Fill by linear interpolation\n"
                          "4. Fill by global constant\n\n"
                          "Input method number [1-4]: "))
                          
	data, input_file = read_file('data.csv') # reading the input file
	header = next(data) # extracting the file header

	result = processChoice(selection, data)
	result.insert(0, header)

	writeToFile(result)
	input_file.close() # closing the input file

	print(f"New File \"{output}\" exported successfully")
except:
    print("something went wrong")