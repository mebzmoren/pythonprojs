#This program has an array of fifteen numbers
#The fifteen numbers will be sorted from lowest to highest
#The numbers will be binned by equal width and equal frequency with 3 bins

#Made by Ellyza Mari Jocson Papas
#Subject: Compsci 35 - A: Data Mining

def equalWidth(array, m):
    a = len(array)
    w = int((max(array) - min(array)) / m)
    min1 = min(array)
    arr = []
    count = 1
    for i in range(0, m + 1):
        arr = arr + [min1 + w * i]
    arri=[]
      
    for i in range(0, m):
        temp = []
        for j in array:
            if j >= arr[i] and j <= arr[i+1]:
                temp += [j]
        arri += [temp]
    print(arri) 

def equalFreq(array, m):    
    a = len(array)
    n = int(a / m)
    for i in range(0, m):
        arr = []
        for j in range(i * n, (i + 1) * n):
            if j >= a:
                break
            arr = arr + [array[j]]
        print(arr)
  
#data to be binned
data = [64, 23, 76, 23, 76, 64, 35, 22, 57, 24, 57, 44, 34, 44, 76]
  
#number of bins
bin = 3

print("\nData to be sorted: ", data)

data.sort()
print("\nSorted data:", data)

print("Number of bins: ",  bin)

print("\nequal width binning")
equalWidth(data, bin)
  
print("\nequal frequency binning")
equalFreq(data, bin)