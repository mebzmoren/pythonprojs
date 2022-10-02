#This is a program that will accept & read a .csv file.
#The .csv file must be in the same folder as this program.
#This program will accept the request of the user to remove the rows with missing data, fill by column average (mean), fill by linear interpolation, and fill by global constant.
#The output will be a .csv file of the user's request.

#Made by Ellyza Mari Jocson Papas
#Subject: Compsci 35 - A: Data Mining

import pandas as pd


##FUNCTTIONS


def removeNullRows(data):             #Removes te rows wth missing data
    return data.dropna()

def fillNullWithMean(data):           #Fills the missing containers with the average mean of the column
    return data.fillna(round(data.mean(), 2))

def fillNullWithInterpolation(data):  #Fills the missing containers by liner interpolation
    return data.interpolate()

def fillNullWithConstant(data):       #Fills the missing containers wth a global constant
    return data.fillna(0)


##MENU


file = input("Input file name: ")   #Accepts the file name of the .csv file. FILE MUST BE IN THE SAME FOLDER AS THIS PROGRAM
selection = input("METHODS:\n"
                  "1. Remove rows with missing data.\n"
                  "2. Fill by column average (mean)\n"
                  "3. Fill by linear interpolation\n"
                  "4. Fill by global constant\n\n"
                  "Input method number [1-4]: ")
                  
try:
    data = pd.read_csv(file, delimiter = ",")     #Reads the .csv file
    selection = int(selection)                  #Accepts the chosen method of the user
    output = "output.csv"                       #File name of the output

    match selection:
        case 1:
                removeNullRows(data).to_csv(output, index = False)
        case 2:
                fillNullWithMean(data).to_csv(output, index = False)
        case 3:
                fillNullWithInterpolation(data).to_csv(output, index = False)
        case 4:
                fillNullWithConstant(data).to_csv(output, index = False)
        case _:
                print("Method not in range 1-4")

    print(f"New File \"{output}\" exported successfully")
except:
    print("Something went wrong")