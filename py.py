import csv
import sys

# check command-line arguments, expect 3 including dna.py
n = len(sys.argv)
if n != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(0)

#database
with open(sys.argv[1], 'r') as database:  
    # datalines
    data_lines = csv.reader(database)  
    data = [row for row in data_lines]  # convert to list of lists, store in data
  # read sequence data, store in string dna
with open(sys.argv[2], 'r') as sequences:
    dna = sequences.read()

counts = [] 
#loop for
for j in range(1, len(data[0])):  
    count = 1
    string = data[0][j]  
    while string * count in dna:  
        count += 1
    counts.append(str(count - 1)) #to get another str i'll go -1

for n in range(1, len(data)):  
    if data[n][1:len(data[0])] == counts:
        print(data[n][0])  
        exit(0)
print('No Match')
