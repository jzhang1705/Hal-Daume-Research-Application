from collections import Counter
import sys

# Segements of code are copied from: https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/

# Let n = total number of words in the document 
# Let k = number of distinct words in the document

# Opens the file in the argument to read
file1 = open(sys.argv[1],"r+") 

# Reads the lines of the file 
Lines = file1.readlines() 

# Appends each word of the document into a list
# Runtime Complexity O(n), Memory Complexity: O(k)
split_it = []
for line in Lines:
    line = line.split()
    for word in line:
        split_it.append(word)
  
# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)
  
# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(10)
print(most_occur)
