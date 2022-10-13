#This program has an array of fifteen numbers
#The fifteen numbers will be sorted from lowest to highest
#The numbers will be binned by equal frequency with 3 bins
#The numbers will be transformed by smoothing using bin by means, boundaries, & median.                                            

#Made by Ellyza Mari Jocson Papas
#Subject: Compsci 35 - A: Data Mining

def equalFreq(array, m):
    a = len(array)
    n = int(a / m)
    binned = []
    for i in range(0, m):
        arr = []
        for j in range(i * n, (i + 1) * n):
            if j >= a:
                break
            arr = arr + [array[j]]
        binned.append(arr)
    return binned

def myRound(x):
    r = x % 1
    if r < 0.5:
        return int(x-r)
    else: 
        return int(x-r+1)

def binMeans(data):
    result = []
    for d in data:
        mean = myRound(sum(d) / len(d))
        newBin = [mean for _ in range(len(d))]
        result.append(newBin)
    return result

def binBoundary(data):
    result = []
    for d in data:
        low = min(d)
        high = max(d)
        newBin = []
        for v in d:
            if (abs(low-v) < abs(high-v)):
                newBin.append(low)
            else:
                newBin.append(high)
        result.append(newBin)
    return result

def binMedian(data):
    result = []
    for d in data:
        n = 0
        if (len(d) % 2 != 0): # if bin has odd number of elements
            n = d[len(d) // 2]
        else: # has even number of elements
            x = d[len(d) // 2]
            y = d[(len(d) // 2) - 1]
            n = (x + y) / 2
        n = myRound(n)
        newBin = [n for _ in d]
        result.append(newBin)
    return result



#data to be binned
data = [64, 23, 76, 23, 76, 64, 35, 22, 57, 24, 57, 44, 34, 44, 76]
  
#number of bins
bin = 3

print("\nData to be sorted: ", data)

data.sort()
print("\nSorted data:", data)

print("\nNumber of bins: ",  bin)
  
print("Partition using equal frequency")
print("Data after binning: ")
data = equalFreq(data, bin)
for d in data:
    print(d)

# make a copy of data for smoothing
# smoothing_data = data[:]

print("\nSmoothing by bin means:")
smoothing_data = binMeans(data)
for d in smoothing_data:
    print(d)

print("\nSmoothing by bin boundary:")
smoothing_data = binBoundary(data)
for d in smoothing_data:
    print(d)

print("\nSmoothing by bin median:")
smoothing_data = binMedian(data)
for d in smoothing_data:
    print(d)